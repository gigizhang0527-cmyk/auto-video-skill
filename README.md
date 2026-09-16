# 🎬 全自动视频创作 Skill

这是一个通用的 **全自动视频创作** 自动化工作流 Skill。**不指定特定的 AI Agent**，任何支持执行 API 调用的 Agent（如 DeepSeek Harness, AutoGPT, MetaGPT 等）均可使用。

## 🚀 一键安装

将以下**完整指令**发送给您的 AI Agent：

```
帮我安装这个项目，安装完成后自动运行配置向导：
https://github.com/gigizhang0527-cmyk/auto-video-skill
```

**💡 Agent 会自动：**
1. 克隆仓库并安装所有依赖（FFmpeg、Whisper 等）
2. 运行安全配置向导（自动打开浏览器和记事本）
3. 逐步引导您完成 API 配置（炳火 → 小米 → Agnes）

**🔒 安全特性：**
- ✅ API Key 直接保存到本地文件，**不会在聊天中显示**
- ✅ 自动打开浏览器到官方注册页面
- ✅ 自动打开记事本编辑配置文件
- ✅ 提供清晰的填写说明和示例

## 📋 使用流程

### 1. 安装配置
发送上述指令给 Agent，按照向导完成 API 配置。

### 2. 验证配置
配置完成后，可以运行检查脚本：
```bash
python scripts/check_config.py
```

### 3. 开始创作
配置完成后，只需告诉 Agent：
```
帮我创作一个视频：[您的文案内容]
```

## 📦 项目结构
```
auto-video-skill/
├── scripts/
│   ├── install.py        # 一键安装（含配置向导）
│   ├── onboarding.py     # 安全配置向导
│   ├── check_config.py   # 配置检查
│   ├── setup.py          # 依赖安装
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
