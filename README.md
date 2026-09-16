# 🎬 全自动视频创作 Skill

这是一个通用的 **全自动视频创作** 自动化工作流 Skill。**不指定特定的 AI Agent**，任何支持执行 API 调用的 Agent（如 DeepSeek Harness, AutoGPT, MetaGPT 等）均可使用。

## ✨ 功能亮点

- **全流程自动化**：从文案脚本、TTS 旁白、SRT 时间轴、参考图生成、动画分镜到 FFmpeg 总装。
- **通用性强**：只要 Agent 能调用 API，就能跑通全流程。
- **精准成本控制**：内置实时价格核对机制（飞书文档），避免意外扣费。
- **严格质控**：内置 V10 方法论（舞台主图 + 图生图链），确保角色和场景一致性。

## 🚀 快速开始

### 1. 一键安装（推荐）
```bash
# 克隆仓库
git clone https://github.com/gigizhang0527-cmyk/auto-video-skill.git
cd auto-video-skill

# 运行安装脚本（自动安装 FFmpeg、Python 依赖、Whisper）
python scripts/setup.py

# 配置 API 密钥
python scripts/configure.py
```

### 2. 手动安装
如果您更喜欢手动安装，请参考 [详细安装指南](INSTALL.md)。

### 3. 使用 Skill
```bash
# 运行完整工作流
python scripts/run_workflow.py --input "您的文案.txt" --project "项目名称"

# 或在 DeepSeek Harness 中使用
/install-skill https://github.com/gigizhang0527-cmyk/auto-video-skill
```

## 📦 依赖说明

本项目需要以下依赖（安装脚本会自动处理）：

| 依赖 | 用途 | 安装方式 |
|------|------|----------|
| **FFmpeg** | 视频处理 | 自动安装或手动下载 |
| **Python 3.8+** | 脚本运行 | 手动安装 |
| **faster-whisper** | 语音转文字 (SRT) | pip install faster-whisper |
| **其他 Python 库** | 图像处理、HTTP 请求等 | pip install -r requirements.txt |

> ⚠️ **注意**：FFmpeg 和 Whisper 都是本地运行的工具，安装脚本会自动下载并配置。

## 📂 项目结构
- `references/`: 核心方法论文档 (V10、封面规范、字幕规范等)
- `scripts/`: 可复用的 Python/PowerShell 脚本
- `templates/`: 项目结构模板

## 📜 许可证
MIT License

## 👨‍💻 作者
- **Jack**: [GitHub Profile](https://github.com/gigizhang0527-cmyk)
- **推荐码**: 使用推荐码注册炳火 API 可获赠额度！
