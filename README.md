# 🎬 全自动视频创作 Skill (开源版)

这是一个基于 DeepSeek Harness 的 **全自动视频创作** 自动化工作流。

## ✨ 功能亮点

- **全流程自动化**：从文案脚本、TTS 旁白、SRT 时间轴、参考图生成、动画分镜到 FFmpeg 总装。
- **多模型协同**：支持炳火 (Seedance/SD2.5)、小米 MiMo (视觉审片)、MiniMax (TTS)。
- **严格质控**：内置 V10 方法论（舞台主图 + 图生图链），确保角色和场景一致性。
- **成本控制**：内置价格核对和实时成本预估，避免意外扣费。

## 🛠️ 快速开始

### 1. 环境准备
请确保已安装：
- [DeepSeek Harness](https://github.com/DeepSeek/DSH)
- [FFmpeg](https://ffmpeg.org/download.html) (需加入 PATH)
- [Python](https://www.python.org/) (可选，用于脚本)
- [HyperFrames](https://github.com/DeepSeek/HyperFrames) (可选，用于动画编排)

### 2. 配置 API 密钥 (必填)
本 Skill 依赖多个外部 API。请访问我们的 **[统一配置文档](https://github.com/gigizhang0527-cmyk/kepu-video-open-source/blob/master/CONFIG.md)** 获取详细的申请指引和配置方法。

**核心依赖：**
| 服务 | 用途 | 注册链接 |
|------|------|----------|
| **炳火 API** | 生图 & 动画 | [点击注册 (含推荐码)](https://api.7tai.cc/register?aff=xJ8H) |
| **小米 MiMo** | 视觉审片 & QC | [小米账号登录](https://account.xiaomi.com/pass/qr/login) |
| **MiniMax** | 语音合成 (TTS) | [MiniMax 开放平台](https://www.minimaxi.com/) |

> ⚠️ **首次运行**：安装后请在配置文件中填入你的 API Key，否则无法生成内容。

### 3. 安装 Skill
```bash
# 在 DeepSeek Harness 中执行
/install-skill https://github.com/gigizhang0527-cmyk/kepu-video-open-source
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
