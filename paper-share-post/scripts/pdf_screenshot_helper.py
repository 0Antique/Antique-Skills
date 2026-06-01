#!/usr/bin/env python3
"""Render PDF pages and crop screenshots for the paper-share-post skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path


def require_fitz():
    try:
        import fitz  # type: ignore
    except ImportError:
        sys.exit(
            "Missing dependency: PyMuPDF. Install it with "
            "`python -m pip install pymupdf`, or render PDF pages with another tool."
        )
    return fitz


def require_pillow():
    try:
        from PIL import Image  # type: ignore
    except ImportError:
        sys.exit(
            "Missing dependency: Pillow. Install it with "
            "`python -m pip install pillow`, or crop images with another tool."
        )
    return Image


def parse_pages(spec: str, page_count: int) -> list[int]:
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            if start > end:
                raise ValueError(f"Invalid page range: {part}")
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    invalid = [p for p in pages if p < 1 or p > page_count]
    if invalid:
        raise ValueError(f"Page(s) out of range 1-{page_count}: {invalid}")
    return sorted(pages)


def safe_paper_name(title: str) -> str:
    title = title.strip()
    title = re.sub(r"\s+", " ", title)
    title = re.sub(r'[\\/:*?"<>|]+', "-", title)
    title = re.sub(r"\s*-\s*", "-", title)
    title = title.strip(" .-_")
    return title or "paper"


def infer_title(pdf_path: Path) -> str:
    fitz = require_fitz()
    doc = fitz.open(pdf_path)
    metadata_title = (doc.metadata or {}).get("title") or ""
    if metadata_title.strip():
        doc.close()
        return metadata_title.strip()

    page_text = doc.load_page(0).get_text("text")
    doc.close()
    lines = [line.strip() for line in page_text.splitlines() if line.strip()]
    if not lines:
        return pdf_path.stem

    ignored = {
        "abstract",
        "introduction",
        "proceedings",
        "references",
    }
    candidates = [
        line
        for line in lines[:20]
        if line.lower() not in ignored and 6 <= len(line) <= 180
    ]
    return candidates[0] if candidates else pdf_path.stem


def parse_archive_date(value: str | None) -> date:
    if value is None:
        return date.today()
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError("Date must use YYYY-MM-DD format.") from exc


def init_output(pdf_path: Path, root_dir: Path, title: str | None, date_value: str | None) -> None:
    archive_date = parse_archive_date(date_value)
    paper_title = title.strip() if title and title.strip() else infer_title(pdf_path)
    paper_name = safe_paper_name(paper_title)
    paper_dir = root_dir / f"{archive_date:%Y}" / f"{archive_date:%m}" / f"{archive_date:%m-%d}-{paper_name}"
    screenshot_dir = paper_dir / "screenshot"
    markdown_path = paper_dir / "论文分享.md"
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    print(f"paper_dir={paper_dir}")
    print(f"screenshot_dir={screenshot_dir}")
    print(f"markdown_path={markdown_path}")
    print(f"title={paper_title}")


def render_pages(pdf_path: Path, out_dir: Path, pages: list[int], dpi: int) -> None:
    fitz = require_fitz()
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    for page_number in pages:
        page = doc.load_page(page_number - 1)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        out_path = out_dir / f"page-{page_number:03d}.png"
        pix.save(out_path)
        print(out_path)


def render_first(pdf_path: Path, out_dir: Path, dpi: int) -> None:
    fitz = require_fitz()
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    zoom = dpi / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    out_path = out_dir / "0 文章第一页PDF截图.png"
    pix.save(out_path)
    print(out_path)


def crop_images(crops_json: Path, out_dir: Path) -> None:
    Image = require_pillow()
    out_dir.mkdir(parents=True, exist_ok=True)
    specs = json.loads(crops_json.read_text(encoding="utf-8"))
    if not isinstance(specs, list):
        raise ValueError("Crop JSON must be a list of crop specs.")

    base = crops_json.parent
    for index, spec in enumerate(specs, start=1):
        source = Path(spec["source"])
        if not source.is_absolute():
            source = base / source
        box = spec["box"]
        if len(box) != 4:
            raise ValueError(f"Crop #{index} must use [left, top, right, bottom].")

        padding = int(spec.get("padding", 0))
        with Image.open(source) as image:
            left, top, right, bottom = [int(v) for v in box]
            left = max(0, left - padding)
            top = max(0, top - padding)
            right = min(image.width, right + padding)
            bottom = min(image.height, bottom + padding)
            if left >= right or top >= bottom:
                raise ValueError(f"Crop #{index} has an empty box after padding.")
            cropped = image.crop((left, top, right, bottom))
            output = out_dir / spec.get("output", f"{index}.png")
            cropped.save(output)
            print(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Create the default date archive output folders.")
    init.add_argument("pdf", type=Path)
    init.add_argument("root_dir", type=Path)
    init.add_argument("--date", help="Archive date in YYYY-MM-DD format. Defaults to today.")
    init.add_argument("--title", help="Paper title to use in the output folder name.")

    first = subparsers.add_parser("first", help="Render the first PDF page.")
    first.add_argument("pdf", type=Path)
    first.add_argument("out_dir", type=Path)
    first.add_argument("--dpi", type=int, default=220)

    render = subparsers.add_parser("render", help="Render selected PDF pages.")
    render.add_argument("pdf", type=Path)
    render.add_argument("out_dir", type=Path)
    render.add_argument("--pages", required=True, help="Page list like 1,3-5.")
    render.add_argument("--dpi", type=int, default=220)

    crop = subparsers.add_parser("crop", help="Crop screenshots from rendered images.")
    crop.add_argument("crops_json", type=Path)
    crop.add_argument("out_dir", type=Path)

    args = parser.parse_args()
    if args.command == "init":
        init_output(args.pdf, args.root_dir, args.title, args.date)
    elif args.command == "first":
        render_first(args.pdf, args.out_dir, args.dpi)
    elif args.command == "render":
        fitz = require_fitz()
        doc = fitz.open(args.pdf)
        pages = parse_pages(args.pages, doc.page_count)
        doc.close()
        render_pages(args.pdf, args.out_dir, pages, args.dpi)
    elif args.command == "crop":
        crop_images(args.crops_json, args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
