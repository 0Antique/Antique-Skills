---
name: blog-share-skills
description: Create Chinese AI/technology blog sharing deliverables from a topic or draft. Use for 技术博客分享, 小红书知识卡片, 博客知识卡片, AI 技术博文可视化, personal-logo HTML cards, card screenshots, social captions, and reusable blog-share workflows.
---

# Blog Share Skills

Create a complete Chinese technical-blog sharing package from a topic or draft:

- a clear technology blog draft when the user only provides a topic
- a single self-contained HTML file containing multiple screenshot-ready knowledge cards with the personal logo embedded
- a folder of rendered PNG screenshots, one image per HTML card
- a social post caption under 500 Chinese characters with hashtags

Write for Chinese-speaking AI and technology readers. Keep the voice professional, concise, practical, and suitable for a personal AI knowledge-sharing account.

## Inputs

Extract these from the user request or ask only for missing essentials:

- Topic, title, or existing blog draft.
- Personal logo or brand assets. By default, use `C:\Users\Antique\.codex\skills\blog-share-skills\示例\2、个人logoAI-logo(16).jpg` unless the user provides another logo or disables branding.
- Target platform, such as 小红书, 技术博客平台, 微信公众号, or general social sharing.
- Output folder, if the user specifies one.

If the topic depends on current libraries, model releases, product APIs, benchmarks, or fast-changing technical facts, verify with current official or primary sources before writing. Do not invent citations, version behavior, API capabilities, experiment results, or code examples.

## Workflow

1. Build or normalize the blog content.
   - If only a topic is provided, research and write a structured Chinese technical blog.
   - If a draft is provided, preserve its technical claims while tightening structure and readability.
   - Favor sections such as 背景, 核心概念, 原理/架构, 工作流程, 实战示例, 对比分析, 使用建议, 总结.

2. Transform the blog into knowledge-card pages.
   - Do not paste long paragraphs directly into cards.
   - Put one core idea on each page.
   - Make every page independently understandable when screenshotted alone.
   - Keep a continuous narrative across pages without requiring readers to remember the previous page.

3. Prepare the personal logo and brand assets.
   - Unless the user provides another logo or explicitly says not to use a logo, use the default personal logo at `C:\Users\Antique\.codex\skills\blog-share-skills\示例\2、个人logoAI-logo(16).jpg`.
   - Embed the logo directly in the HTML as a base64 `data:image/jpeg` URI. Do not reference the absolute local logo path from the HTML because screenshots and sharing should not break when files move.
   - Place the logo prominently on the square cover and use a smaller logo mark in later pages, usually in a corner or footer.
   - If the default logo file is missing and the user did not provide another logo, mention this briefly and use a text brand mark instead.

4. Generate one complete HTML file.
   - Use plain HTML + CSS in one file; put CSS in a `<style>` tag.
   - Do not rely on external frameworks, remote fonts, remote images, or CDN assets.
   - Use fixed card dimensions to make browser screenshots stable.
   - Use separate `section.card` containers for each page so the screenshot script can export one image per page.
   - Keep markup easy to edit later.

5. Render HTML knowledge cards to PNG screenshots.
   - Always create a screenshot folder, normally `<output-folder>/html知识卡片截图`.
   - Export each `section.card` as a separate PNG named `1.png`, `2.png`, `3.png`, ... in reading order.
   - Prefer the bundled script with Codex bundled Node: `C:\Users\Antique\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe C:\Users\Antique\.codex\skills\blog-share-skills\scripts\render_cards.js --html <html-file> --out <output-folder>\html知识卡片截图`.
   - The screenshot script auto-detects local Chrome/Edge; if needed, pass `--browser <chrome-or-edge-path>`. If the bundled script cannot run, use another browser automation path, but still save individual card screenshots and verify the count.

6. Create the post caption.
   - Summarize the whole card set in natural Chinese.
   - Keep the caption under 500 Chinese characters.
   - End with relevant hashtags, for example `#人工智能 #AI #技术博客 #知识分享`.

7. Verify before final response.
   - Check every page for overcrowding, clipped text, inconsistent alignment, and broken visual rhythm.
   - Confirm the personal logo is visible on the cover and appears consistently on later pages.
   - Confirm code blocks, commands, and directory trees are technically accurate and readable.
   - Confirm the HTML can be opened directly in a browser.
   - Confirm screenshot PNG files exist and their count matches the number of section.card pages.
   - Confirm the caption is under 500 Chinese characters and ends with hashtags.

## Card Structure

Use this structure unless the user specifies a different one:

1. Square cover page, 1:1, for 小红书 first image.
2. Landscape cover page, 4:3, for blog cover or backup cover.
3. Concept explanation page, 4:3.
4. Core structure or architecture breakdown page, 4:3.
5. Workflow or step-by-step logic page, 4:3.
6. Comparison page, 4:3, when related concepts are useful.
7. Practical page with code, commands, directory structure, or operational steps, 4:3.
8. Summary page with value, scenarios, and one-sentence conclusion, 4:3.

Adjust the number of pages to fit the content, but avoid dense cards.

## Visual Direction

Use a warm, clean, recognizable personal AI-blogger style:

- Warm yellow for highlights, title decoration, labels, and soft glow.
- Cyan-blue for technical lines, borders, code blocks, and flow arrows.
- Coffee brown for main titles, emphasis, and stable brand recognition.
- White or warm off-white backgrounds for clean screenshots.

Suggested colors:

- Main: `#F7C948`, `#FFD966`
- Secondary: `#2CB7C9`, `#3AAFC8`
- Accent: `#5B2E1E`, `#6B3A2A`
- Background: `#FFF8E8`, `#FFFDF7`
- Border: `#E8D8B8`, `#BFE7EA`
- Body text: `#3B2A22`

Avoid dark cyberpunk styling, large black backgrounds, excessive gradients, and heavy shadows.

## Brand Elements

Always use a logo unless the user explicitly disables branding:

- Default logo: `C:\Users\Antique\.codex\skills\blog-share-skills\示例\2、个人logoAI-logo(16).jpg`.
- If the user provides another logo, use the user-provided logo instead of the default.
- Embed the logo in the HTML as a base64 data URI so the HTML remains self-contained.
- Place the logo prominently on the cover.
- Use a smaller version in later pages, usually in a corner or footer.
- Abstract visual motifs from the logo when helpful, such as smile circles, headset/microphone, book, lightbulb, stars, or light points.
- Match the logo's mood without copying it literally.
- If no logo file is available, use a simple text brand mark and mention the missing logo in the final response.

## Layout Rules

- Keep titles large and clear, subtitles short, and body text sentence-like rather than paragraph-heavy.
- Use cards, labels, rounded modules, process arrows, icon-like elements, and code blocks.
- Leave enough whitespace on every page.
- Add page numbers and a small account mark or fixed slogan in the footer when useful.
- Use emoji or simple inline SVG only as light decoration; do not overuse them.
- Use clear code-block styling for code, commands, and directory trees.

## Final Response

Return the absolute paths to generated files, normally:

- the blog draft, if created
- the HTML knowledge-card file
- the screenshot folder containing rendered PNG cards
- the social post caption file, if saved separately

Mention any unresolved facts or missing brand assets briefly. Do not paste the full HTML into the final response unless the user asks for an inline preview.

