---
name: paper-share-post
description: Create reusable Chinese AI paper-sharing deliverables from a research paper PDF for native Chinese readers. Use when Codex is asked to process a 论文 PDF for 论文分享、自媒体帖子、博客、paper reading notes, or WeChat/Xiaohongshu-style sharing, including extracting/cropping the paper homepage, figures, and tables, then writing a concise Chinese Markdown post with source, link, paper title, research background, contributions, method, and one-sentence summary.
---

# Paper Share Post

Convert one research-paper PDF into a date-archived share-ready bundle: paper screenshots plus a Chinese Markdown sharing post.

The target audience's native language is Chinese. Write for Chinese-speaking AI readers using natural Chinese phrasing, not translated English sentence structure.

## Reference Loading

- Read `references/post-style.md` before drafting or revising the Markdown post.
- Read `references/screenshot-spec.md` before producing or checking screenshots.
- Use `scripts/pdf_screenshot_helper.py` when PDF rendering or image cropping can be automated.

## Inputs

Require the paper PDF. Extract metadata from the PDF first, then ask only for missing information that cannot be inferred safely:

- paper source or venue, such as `AAAI 2026`, `IJCAI 2026`, `arXiv`, or a project page
- canonical paper URL
- output folder, if the user has a specific location
- screenshot scope, if the user wants fewer than all main-text figures and tables

Do not invent source, link, title, task setting, method name, experiment result, or claimed contribution. If a detail is uncertain, mark it as unresolved and ask before finalizing.

## Output Layout

Create a per-paper output folder unless the user specifies one. The default root is the current working directory. Use the current date unless the user specifies a date. Derive `paper-name` from the paper title after metadata extraction, using a readable filesystem-safe short name:

```text
YYYY/
└── MM/
    └── MM-DD-论文名/
        ├── screenshot/
        │   ├── 0 文章第一页PDF截图.png
        │   ├── 1.png
        │   ├── 2.png
        │   └── ...
        └── 论文分享.md
```

Example for a paper processed on 2026-06-01:

```text
2026/
└── 06/
    └── 06-01-FedALT/
        ├── screenshot/
        │   ├── 0 文章第一页PDF截图.png
        │   ├── 1.png
        │   └── 2.png
        └── 论文分享.md
```

Do not use the old `<paper-name>-share/` or `screenshots/` layout unless the user explicitly asks for it. Use `screenshot/` exactly, singular.

The final paths must resolve to:

```text
YYYY/MM/MM-DD-论文名/screenshot/
YYYY/MM/MM-DD-论文名/论文分享.md
```

For example:

```text
2026/06/06-01-论文名/screenshot/
2026/06/06-01-论文名/论文分享.md
```

Inside `screenshot/`:

```text
screenshot/
│   ├── 0 文章第一页PDF截图.png
│   ├── 1.png
│   ├── 2.png
│   └── ...
```

Use `0 文章第一页PDF截图.png` for the full first page. Number figure and table screenshots as `1.png`, `2.png`, ... in the order they should appear in the share post, normally the order of appearance in the main paper.

## Workflow

1. Inspect the PDF.
   - Identify title, authors if useful, source or venue, URL, abstract, introduction problem, method section, contributions, key experiments, conclusion, and all main-text figures/tables.
   - Prefer the paper's own wording for method and contribution names, then rewrite in accessible Chinese.
   - Decide the output folder name only after identifying the title. Keep it short, stable, and readable; replace path separators and unsafe characters with `-`.

2. Create the output folder.
   - Default path format is `YYYY/MM/MM-DD-论文名/`.
   - Put all images in `YYYY/MM/MM-DD-论文名/screenshot/`.
   - Put the Markdown post at `YYYY/MM/MM-DD-论文名/论文分享.md`.
   - If the user gives an output root, create the `YYYY/MM/MM-DD-论文名/` tree under that root.

3. Produce screenshots.
   - Capture the PDF first page as `0 文章第一页PDF截图.png`.
   - Crop every main-text figure and table unless the user narrows scope.
   - Keep captions when they help interpret the figure/table; otherwise crop tightly around the visual content.
   - Use readable resolution, no cut-off labels, no unrelated column text, and consistent margins.
   - If automatic figure detection is unreliable, render relevant pages and crop manually by pixel coordinates.

4. Draft `论文分享.md`.
   - Follow `references/post-style.md` exactly for structure, tone, length, and title constraints.
   - Keep the whole post within 900 Chinese characters.
   - Use natural Chinese, light emoji, and an AI blogger voice: clear, practical, and easy to scan for Chinese readers.
   - Explain the research background first, then contributions, then method, then a one-sentence takeaway.
   - Avoid evaluation hype that the paper does not support.

5. Verify before final response.
   - Confirm the title starts with `论文分享：` and is no more than 20 characters when feasible.
   - Confirm all metadata placeholders are filled or explicitly listed as unresolved.
   - Confirm the Markdown has the required sections in order.
   - Confirm the Markdown is saved exactly as `YYYY/MM/MM-DD-论文名/论文分享.md`.
   - Confirm screenshots are saved exactly under `YYYY/MM/MM-DD-论文名/screenshot/`.
   - Confirm screenshot filenames match the required convention.
   - Confirm the post is under 900 Chinese characters.

## Screenshot Helper

Use the bundled helper for repeatable rendering/cropping:

```bash
python scripts/pdf_screenshot_helper.py init paper.pdf out --date 2026-06-01 --title "论文名"
python scripts/pdf_screenshot_helper.py first paper.pdf out/2026/06/06-01-论文名/screenshot
python scripts/pdf_screenshot_helper.py render paper.pdf out/rendered --pages 1,3-5 --dpi 220
python scripts/pdf_screenshot_helper.py crop crops.json out/2026/06/06-01-论文名/screenshot
```

`init` creates `YYYY/MM/MM-DD-论文名/screenshot/` and prints the paper folder, screenshot folder, and Markdown path. If `--title` is omitted, it tries to infer a title from PDF metadata or the first page text; verify the inferred folder name before finalizing.

`crop` expects image pixel coordinates:

```json
[
  {
    "source": "out/rendered/page-003.png",
    "box": [120, 240, 1420, 980],
    "output": "1.png",
    "padding": 12
  }
]
```

Coordinates are `[left, top, right, bottom]` in pixels. Resolve relative `source` paths from the crop JSON file location.

## Final Response

Return the absolute paths to:

- the Markdown post
- the screenshot folder
- any unresolved metadata or screenshots that need user confirmation

Keep the final response concise. Do not paste the full post unless the user asks to preview it in chat.
