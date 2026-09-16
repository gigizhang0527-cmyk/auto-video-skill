# 🎬 全自动视频创作 Skill

这是一个通用的 **全自动视频创作** 自动化工作流 Skill。**不指定特定的 AI Agent**，任何支持执行 API 调用的 Agent（如 DeepSeek Harness, AutoGPT, MetaGPT 等）均可使用。

## 🚀 三步上手

### 1. 安装 Skill
将以下链接发送给您的 AI Agent，并附带指令：
```
帮我安装这个项目，安装完成后自动运行 python scripts/install.py 进行配置：
https://github.com/gigizhang0527-cmyk/auto-video-skill
```

**💡 提示：** 
- Agent 会自动克隆仓库并安装依赖
- 安装完成后会**自动运行**安全配置向导
- 向导会逐步引导您完成 API 配置，**不会在聊天中显示 API Key**

### 2. 配置 API（安全方式）
安装完成后，运行安全配置向导：
```bash
python scripts/install.py
```

**安全特性：**
- ✅ 自动打开浏览器到注册页面
- ✅ 自动打开记事本编辑配置文件
- ✅ API Key 直接保存到本地，**不会在聊天中显示**
- ✅ 逐步引导（炳火 → 小米 → Agnes）

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
│   ├── install.py        # 一键安装（安全配置向导）
│   ├── onboarding.py     # 安全引导脚本
│   ├── check_config.py   # 配置检查
│   ├── setup.py          # 依赖安装
│   └── run_workflow.py   # 主工作流
├── references/           # 方法论文档
└── README.md             # 本文件
```

## 🔒 安全说明
本项目**绝不会**在聊天框中要求您输入 API Key。所有敏感信息都通过以下方式处理：
1. 自动打开浏览器到官方注册页面
2. 自动打开记事本编辑本地配置文件
3. API Key 直接写入 `~/.agents/config/auto-video-skill-config.json`

## 💡 特性
- **全流程自动化**：从文案到成片，全程无需人工干预
- **精准成本控制**：内置实时价格核对，避免意外扣费
- **严格质控**：V10 方法论确保角色和场景一致性

## 📜 许可证
MIT License

## 👨‍💻 作者
- **Jack**: [GitHub Profile](https://github.com/gigizhang0527-cmyk)
- **推荐码**: 使用推荐码注册炳火 API 可获赠额度！
