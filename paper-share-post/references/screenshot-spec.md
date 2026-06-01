# Screenshot Specification

Use this reference when creating or reviewing screenshot outputs. Save screenshots under `YYYY/MM/MM-DD-论文名/screenshot/` by default.

## Required Screenshots

- `0 文章第一页PDF截图.png`: full screenshot of the first PDF page.
- `1.png`, `2.png`, ...: screenshots of the paper's figures and tables.

Default scope:

- Include main-paper figures in order: Figure 1, Figure 2, ...
- Include main-paper tables in order: Table 1, Table 2, ...
- Include appendix figures/tables only when the user asks or when the main paper depends on them.

## Quality Criteria

- Render at high enough resolution for social media reading, usually 200-300 DPI.
- Crop tightly enough to remove unrelated paragraphs, headers, and page margins.
- Keep axis labels, legends, table headers, and important captions readable.
- Include the caption only when it helps users understand the visual quickly.
- Keep a small consistent margin around each crop.
- Avoid cutting off symbols, legends, footnotes, or table borders.
- Use PNG unless the user asks otherwise.

## Practical Cropping Workflow

1. Create the output directory as `YYYY/MM/MM-DD-论文名/screenshot/`.
2. Render the first page directly to `0 文章第一页PDF截图.png`.
3. Skim the PDF and list every target figure/table with page number.
4. Render target pages to temporary page images.
5. Crop target regions from rendered page images using pixel coordinates.
6. Name outputs sequentially by sharing order.
7. Visually inspect the final files before reporting completion.

If figure/table detection is uncertain, ask the user whether to include ambiguous visuals rather than silently skipping them.
