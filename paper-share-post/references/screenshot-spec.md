# Screenshot Specification

Use this reference when creating or reviewing screenshot outputs.

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

1. Render the first page directly to `0 文章第一页PDF截图.png`.
2. Skim the PDF and list every target figure/table with page number.
3. Render target pages to temporary page images.
4. Crop target regions from rendered page images using pixel coordinates.
5. Name outputs sequentially by sharing order.
6. Visually inspect the final files before reporting completion.

If figure/table detection is uncertain, ask the user whether to include ambiguous visuals rather than silently skipping them.
