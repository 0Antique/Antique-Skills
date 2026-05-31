---
name: paper-search-assistant
description: Search and curate recent research paper collections by target conference set, year range, and research topic, then return a verified Chinese table with title, conference-year, keywords, paper link, and open-source code status. Use when the user asks to find papers from CCF-A/AI conferences, top conferences such as ICLR, ICML, NeurIPS/NIPS, ACL, AAAI, KDD, CVPR, or strong B conferences such as ICASSP, EMNLP, IJCAI, especially for a topic-focused literature list or paper collection.
---

# Paper Search Assistant

## Goal

Find papers for a user-specified research topic and conference scope, prioritizing recent papers and official sources, then summarize them as a clean Chinese table.

## Before Searching

Read `references/search-guidelines.md` before doing the search.

Extract these inputs from the user request:

- Topic or keywords, such as `federated learning`, `LLM agent`, `CV`, `RAG`, or Chinese equivalents.
- Conference scope, such as `三大A`, `CCF-A`, `ICLR/ICML/NeurIPS`, `ACL/AAAI/KDD/CVPR`, or named conferences.
- Year scope. If absent, search recent years first and prefer newer papers.
- Desired count. If absent, target 10-20 high-relevance papers.

Ask only for the missing topic if it cannot be inferred. If the conference or year scope is missing, use the defaults in `references/search-guidelines.md` and state the assumption.

## Search Workflow

1. Use web search. Paper lists, conference acceptances, paper links, and code availability are current information and must be verified online.
2. Search official conference/proceedings sources first. Use arXiv only as a fallback or companion link when an official paper page is not available.
3. For each candidate, verify that the paper actually matches both the target topic and the requested conference/year.
4. Check code availability from credible sources: official project page, paper page, author GitHub, or Papers with Code. Do not mark code as open-source from an unverified third-party mirror.
5. Deduplicate by title. Prefer the final conference version over arXiv preprints.
6. Sort by newest year first, then by conference priority and topic relevance.

## Output Format

Return a short Chinese note describing the search scope, then a Markdown table:

```markdown
| 标题 | 会议-年份 | 关键词 | 论文链接 | 是否开源代码 |
| --- | --- | --- | --- | --- |
| 《...》 | ICLR-2026 | FL，CV，Agent | 官方链接或 arXiv 链接 | 是：https://github.com/... |
```

Rules:

- Use Chinese for the surrounding explanation and keywords.
- Keep titles exact. Wrap paper titles in `《》`.
- Use `NeurIPS` for recent papers, but accept user wording `NIPS`.
- In `论文链接`, prefer the official publication/proceedings/OpenReview/CVF/ACL/ACM/PMLR page; use arXiv if the official page is unavailable.
- In `是否开源代码`, use `是：<code link>` only when a credible code repository is found. Use `否（未检索到）` when not found after checking.
- Include source links in table cells whenever possible.
- If fewer papers are found than requested, say so and explain the limiting condition.

## Quality Check

Before finalizing:

- Confirm every row has title, conference-year, topic keywords, paper link, and code status.
- Confirm every included paper is in the requested conference/year scope.
- Confirm links are not invented and code links are not confused with paper links.
- Confirm the table is useful for copying into notes or spreadsheets.
