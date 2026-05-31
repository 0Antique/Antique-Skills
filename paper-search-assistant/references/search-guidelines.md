# Search Guidelines

## Defaults

If the user does not specify conference scope, search in this order:

1. 三大 A: ICLR, ICML, NeurIPS.
2. Other common CCF-A or top AI conferences: ACL, AAAI, KDD, CVPR.
3. Strong B or field-important conferences when useful: ICASSP, EMNLP, IJCAI.

If the user does not specify years, prefer the newest available conference years first. Use the current date to avoid treating future proceedings as finalized. If a conference year is not yet published, say it is not available instead of fabricating entries.

If the user does not specify count, return 10-20 papers. Use fewer if the topic is narrow and verified candidates are limited.

## Preferred Sources

Use official or stable sources first:

- ICLR: OpenReview venue pages and accepted paper pages.
- ICML: PMLR proceedings and official ICML accepted paper lists.
- NeurIPS: official NeurIPS proceedings.
- ACL / EMNLP: ACL Anthology.
- AAAI: AAAI proceedings or official conference pages.
- KDD: ACM Digital Library or official KDD accepted paper pages.
- CVPR: CVF Open Access.
- IJCAI: IJCAI proceedings.
- ICASSP: IEEE Xplore or official proceedings pages.
- arXiv: use as fallback, preprint companion, or when official proceedings are not yet available.
- Code: official project page, author GitHub, Papers with Code, or links from the paper page.

## Query Patterns

Use combinations of conference, year, and topic:

- `site:openreview.net ICLR 2025 "<topic>"`
- `site:proceedings.mlr.press ICML 2025 "<topic>"`
- `site:proceedings.neurips.cc NeurIPS 2025 "<topic>"`
- `site:aclanthology.org EMNLP 2025 "<topic>"`
- `site:openaccess.thecvf.com CVPR 2025 "<topic>"`
- `site:dl.acm.org KDD 2025 "<topic>"`
- `"<paper title>" code GitHub`
- `"<paper title>" Papers with Code`

When Chinese topic terms are provided, translate them into likely English search terms and keep both in mind. Example: `联邦学习` -> `federated learning`; `大模型智能体` -> `LLM agents`; `检索增强生成` -> `retrieval augmented generation` or `RAG`.

## Relevance Filter

Include a paper only if the topic is central, not just mentioned in passing. Evidence can come from title, abstract, keywords, paper page, or author-provided summary.

Prefer:

- Papers whose title or abstract directly names the topic.
- Papers from the requested venue/year.
- Papers with official pages and clear metadata.
- Papers that are methodologically relevant to the user's theme, even if the exact keyword differs.

Avoid:

- Workshop papers unless the user asks for workshops.
- Preprints that were not accepted to the requested conference.
- Papers from adjacent topics without a clear connection.
- Code links from unrelated reimplementations unless explicitly labeled as unofficial.

## Table Semantics

`会议-年份` examples:

- `ICLR-2025`
- `NeurIPS-2024`
- `CVPR-2026`

`关键词` should be 2-5 concise Chinese/English mixed terms, separated by Chinese commas:

- `FL，隐私计算，个性化`
- `LLM Agent，工具调用，规划`
- `RAG，长上下文，检索`

`论文链接` should be one link, with preference:

1. Official proceedings or conference paper page.
2. OpenReview / ACL Anthology / CVF / PMLR / ACM / IEEE page.
3. arXiv page.

`是否开源代码` values:

- `是：https://github.com/...`
- `是：<official project page>`
- `否（未检索到）`

Do not use `是` without a link.

## Final Response Pattern

Start with:

`检索范围：<conference scope>，年份：<year scope>，主题：<topic>。优先使用官方论文页，arXiv 作为补充。`

Then provide the table. If there are caveats, place them after the table under `说明：`.
