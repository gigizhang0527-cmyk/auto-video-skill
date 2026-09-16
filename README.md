# 🎬 全自动视频创作 Skill

这是一个通用的 **全自动视频创作** 自动化工作流 Skill。**不指定特定的 AI Agent**，任何支持执行 API 调用的 Agent（如 DeepSeek Harness, AutoGPT, MetaGPT 等）均可使用。

## 🚀 三步上手

### 1. 安装 Skill
将以下链接发送给您的 AI Agent：
```
https://github.com/gigizhang0527-cmyk/auto-video-skill
```
Agent 会自动拉取项目并安装所需依赖（FFmpeg、Whisper 等）。

### 2. 配置 API
安装完成后，Agent 会**逐步引导**您完成 API 配置：
1. **炳火 API**：用于生图 → [点击注册](https://api.7tai.cc/register?aff=xJ8H)
2. **小米 MiMo**：用于审片 & TTS → [点击注册](https://platform.xiaomimimo.com?ref=YGUXWL)
3. **Agnes**：用于视频生成 → [点击注册](https://www.agnes-ai.com/)

> ⚠️ **注意**：请按顺序完成注册，每完成一个平台后，将 API Key 告诉 Agent，Agent 会帮您保存。

### 3. 运行创作
当所有 API 配置完成后，只需告诉 Agent：
```
帮我创作一个视频：[您的文案内容]
```
Agent 会自动执行全流程：文案 → TTS → SRT → 参考图 → 动画 → 成片。

## 📦 项目结构
```
auto-video-skill/
├── scripts/
│   ├── setup.py          # 一键安装依赖
│   ├── configure.py      # API 配置向导
│   └── run_workflow.py   # 主工作流
├── references/           # 方法论文档
└── README.md             # 本文件
```

## 💡 特性
- **全流程自动化**：从文案到成片，全程无需人工干预
- **精准成本控制**：内置实时价格核对，避免意外扣费
- **严格质控**：V10 方法论确保角色和场景一致性

## 📜 许可证
MIT License

## 👨‍💻 作者
- **Jack**: [GitHub Profile](https://github.com/gigizhang0527-cmyk)
- **推荐码**: 使用推荐码注册炳火 API 可获赠额度！
