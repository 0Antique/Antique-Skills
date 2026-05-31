# Antique-Skills

A personal collection of custom Claude Skills maintained by the repository owner.

This repository contains skills for Chinese technical blog sharing and research-paper workflows. Each skill lives in its own folder and is defined by a `SKILL.md` file, sometimes with supporting references or scripts.

[Read the Simplified Chinese version](./README-zh.md)

## What’s in this repo

| Skill | Purpose |
| --- | --- |
| `blog-share-skills` | Create Chinese AI/technology blog-sharing packages, including structured blog drafts, self-contained HTML knowledge cards, screenshot-ready page exports, and short social captions. |
| `paper-search-assistant` | Search and curate recent research papers by topic, conference scope, and year range, then return a verified Chinese table with paper links and code status. |
| `paper-share-post` | Turn a research paper PDF into a Chinese sharing bundle with screenshots and a concise Markdown post for readers. |

## How to use a skill

1. Open Claude.
2. Ask Claude to use the skill that matches your task, or invoke the skill by name when supported.
3. Follow the prompts the skill asks for, such as topic, target platform, year range, paper PDF, or output folder.
4. Claude will then follow the skill’s workflow and produce the requested deliverable.

## Repository structure

```text
Antique-Skills/
├── README.md
├── README-zh.md
├── blog-share-skills/
│   └── SKILL.md
├── paper-search-assistant/
│   └── SKILL.md
└── paper-share-post/
    └── SKILL.md
```

## Adding a new skill

Create a new folder for the skill, then add a `SKILL.md` file that explains:

- what the skill is for
- when it should be used
- what inputs it needs
- the recommended workflow
- the expected output format

If the skill depends on helper files, keep them inside the same skill folder.
