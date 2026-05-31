# Paper Share Post Style

Use this reference when writing `论文分享.md`.

## Required Structure

```markdown
论文分享：xxxx

论文来源：【论文来源】

论文地址：【文章链接】

文章名称：《标题名》

研究背景 🔍

...

主要贡献 ✨

* ...
* ...
* ...

方法 🧠

...

一句话总结 🚀

...
```

## Writing Rules

- Write in Chinese.
- Assume the target audience's native language is Chinese; use natural Chinese expressions and avoid stiff translated-English phrasing.
- Title format must be `论文分享：xxxx`.
- Keep the title attractive and specific; keep total title length within 20 characters when feasible.
- Keep the entire post under 900 Chinese characters.
- Use a few emoji to improve readability, but do not overuse them.
- Write for Chinese-speaking AI self-media/blog readers: clear, concrete, and readable.
- Preserve the paper's actual method name, task setting, and key claims.
- Prefer short paragraphs and 2-4 contribution bullets.
- Explain why the problem matters before describing the method.
- End with one concise sentence that captures the paper's core idea.

## Source Prompt

The user's original writing prompt:

```text
我是一个人工智能博主，在自媒体平台发布这篇论文的阅读分享，请你写一个博客。

为文章取一个标题，格式为：
论文分享：xxxx

用中文进行描述，标题吸睛。标题总字数20字以内（严格要求）

开头固定的内容：
论文来源：【论文来源】（AAAI-26，IJCAI 2026等）
论文地址：【文章链接】（https://arxiv.org/abs/2306.05685，贴出论文链接）
文章名称：【标题名】（《Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena》)

研究背景（什么方向，存在什么问题需要解决）
主要贡献（文章的主要贡献）
方法（本文提出的方法的名称，是怎么做的）
一句话总结（简短总结文章）

必须严格控制在900字以内。
使用一些表情符号，增强可阅读性。
```

## Example Style

```markdown
论文分享：联邦场景的大语言模型LoRA 微调

论文来源：【AAAI 2026】

论文地址：【https://arxiv.org/abs/2503.11880】

文章名称：《FedALT: Federated Fine-Tuning through Adaptive Local Training with Rest-of-World LoRA》

研究背景 🔍

这篇论文关注联邦学习场景下的大语言模型 LoRA 微调。在医疗、金融、企业等场景中，数据往往分布在不同机构，不能直接共享。联邦学习可以在保护隐私的前提下，让多个客户端协同微调大模型。但现有联邦 LoRA 方法大多基于 FedAvg：各客户端本地训练 LoRA，再把参数上传到服务器平均，得到一个全局 LoRA。问题是，现实中的客户端任务可能完全不同。此时简单平均参数会带来跨客户端干扰 😵，甚至破坏本地任务性能。

主要贡献 ✨

* 指出现有 FedAvg 式联邦 LoRA 微调在任务异构场景下容易产生 harmful cross-client interference。
* 提出 FedALT，一种新的个性化联邦 LoRA 微调框架，避免用全局平均 LoRA 覆盖客户端本地适配能力。
* 设计 Rest-of-World LoRA 和 adaptive mixer，让客户端既能吸收其他客户端的有用知识，又能保留自己的任务个性化能力。

方法 🧠

FedALT 中，每个客户端维护两个 LoRA：Individual LoRA 学习本客户端任务；RoW LoRA 由其他客户端的 Individual LoRA 聚合得到，表示“外部共享知识”。关键在于，RoW LoRA 在本地训练时是冻结的，不参与更新，因此不会像 FedAvg 那样反复干扰本地模型。此外，FedALT 引入 adaptive mixer，根据每个输入动态决定更依赖 Individual LoRA，还是 RoW LoRA，实现输入级自适应融合 ⚖️。

一句话总结 🚀

FedALT 的核心是：用冻结的“其他客户端知识”辅助本地 LoRA，再通过动态 mixer 自适应融合，从而在联邦微调中减少干扰、增强个性化。
```
