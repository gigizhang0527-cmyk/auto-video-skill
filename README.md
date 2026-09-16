# 🎬 全自动视频创作 Skill

这是一个通用的 **全自动视频创作** 自动化工作流 Skill。

## 🚀 一键安装

将以下**完整指令**发送给您的 AI Agent：

```
帮我安装这个项目，安装完成后自动运行配置向导：
https://github.com/gigizhang0527-cmyk/auto-video-skill
```

## 🛠️ 核心功能

- **全流程自动化**：文案 → TTS → SRT → 参考图 → 动画 → 成片
- **统一 API 平台**：
  - **炳火 API**：负责生图 (GPT IMAGE 2.5) + 视频生成 (Seedance)
  - **小米 MiMo**：负责视觉审片 + TTS 语音合成
- **智能验证**：配置向导会自动验证 API Key 是否有效，无效则不允许进入下一步

## 📦 依赖说明

- **FFmpeg**：视频处理 (自动安装)
- **Whisper**：语音转文字 (自动安装)

## 📜 许可证
MIT License
