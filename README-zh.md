# Antique-Skills

作者：Antique

这是一个我个人自定义的 Claude Skills 仓库。

这个仓库收录了面向中文技术写作、论文检索与论文分享的技能。每个技能都放在独立目录中，并通过 `SKILL.md` 进行定义，部分技能还会附带引用资料或脚本。

[View the English version](./README.md)

## 仓库内容

| 技能 | 用途 |
| --- | --- |
| `blog-share-skills` | 生成中文 AI / 技术博客分享产物，包括结构化博客草稿、自包含的 HTML 知识卡片、可截图页面导出和社媒短文案。 |
| `paper-search-assistant` | 按主题、会议范围和年份检索并整理论文，输出经过核验的中文表格，包含论文链接和开源代码状态。 |
| `paper-share-post` | 把一篇论文 PDF 转成中文分享包，包含截图和适合读者阅读的 Markdown 分享文。 |

## 如何使用技能

1. 打开 Claude。
2. 根据任务选择对应技能，或者在支持的环境里直接调用技能名。
3. 按技能提示补充必要信息，例如主题、目标平台、年份范围、论文 PDF 或输出目录。
4. Claude 会按照技能中的工作流完成并输出结果。

## 仓库结构

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

## 如何新增技能

为新技能创建一个目录，并添加一个 `SKILL.md`，说明：

- 这个技能是做什么的
- 什么时候应该使用
- 需要哪些输入
- 推荐的工作流程
- 预期输出格式

如果技能依赖辅助文件，也一并放在同一个技能目录下。
