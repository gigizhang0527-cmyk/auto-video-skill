# 🎬 全自动视频创作 Skill

这是一个通用的 **全自动视频创作** 自动化工作流 Skill。**不指定特定的 AI Agent**，任何支持执行 API 调用的 Agent（如 DeepSeek Harness, AutoGPT, MetaGPT 等）均可使用。

## ✨ 功能亮点

- **全流程自动化**：从文案脚本、TTS 旁白、SRT 时间轴、参考图生成、动画分镜到 FFmpeg 总装。
- **通用性强**：只要 Agent 能调用 API，就能跑通全流程。
- **精准成本控制**：内置实时价格核对机制（飞书文档），避免意外扣费。
- **严格质控**：内置 V10 方法论（舞台主图 + 图生图链），确保角色和场景一致性。

## 🛠️ 快速开始

### 1. 环境准备
请确保运行环境已安装：
- [FFmpeg](https://ffmpeg.org/download.html) (需加入 PATH)
- [Python](https://www.python.org/) (可选，用于脚本)

### 2. 配置 API 密钥 (必填)
本 Skill 依赖以下 API 服务。请在首次运行前完成配置。

**核心依赖：**
| 服务 | 用途 | 注册链接 | 价格参考 |
|------|------|----------|----------|
| **炳火 API** | 生图 (GPT IMAGE 2.5) | [点击注册](https://api.7tai.cc/register?aff=xJ8H) | [价格表 (飞书)](https://mcn1eoufbabt.feishu.cn/wiki/D0XMwr2EXibFsQkd2Z0ctO5WnUg) |
| **小米 MiMo** | 视觉审片 & QC & TTS | [小米开放平台](https://platform.xiaomimimo.com/console/api-keys) | - |
| **Agnes** | 视频生成 (参考) | [Agnes 官网](https://www.agnes-ai.com/) | - |

> ⚠️ **首次运行**：Agent 会自动引导您填写 API Key。配置文件通常位于 `~/.agents/config/auto-video-skill-config.json`。

### 3. 安装 Skill
```bash
# 在您的 Agent 中执行安装命令 (以 DeepSeek Harness 为例)
/install-skill https://github.com/gigizhang0527-cmyk/auto-video-skill
```

## 📂 项目结构
- `references/`: 核心方法论文档 (V10、封面规范、字幕规范等)
- `scripts/`: 可复用的 Python/PowerShell 脚本
- `templates/`: 项目结构模板

## 📜 许可证
MIT License

## 👨‍💻 作者
- **Jack**: [GitHub Profile](https://github.com/gigizhang0527-cmyk)
- **推荐码**: 使用推荐码注册炳火 API 可获赠额度！
