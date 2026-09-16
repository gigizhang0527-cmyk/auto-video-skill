# 🚀 安装指南

本指南将帮助您快速安装和配置 **全自动视频创作 Skill**。

## 📋 前置条件

在安装之前，请确保您的系统满足以下条件：

### 必需条件
1. **操作系统**：Windows 10/11, macOS 10.15+, 或 Linux (Ubuntu 18.04+)
2. **Python 3.8+**：用于运行脚本和 Whisper
3. **FFmpeg**：用于视频处理
4. **网络连接**：用于下载依赖和调用 API

### 可选条件
1. **Git**：用于克隆仓库
2. **CUDA/GPU**：用于加速 Whisper 语音识别（可选）

## 🛠️ 安装步骤

### 方法一：自动安装（推荐）

1. **克隆仓库**
   ```bash
   git clone https://github.com/gigizhang0527-cmyk/auto-video-skill.git
   cd auto-video-skill
   ```

2. **运行安装脚本**
   ```bash
   python scripts/setup.py
   ```

   安装脚本将自动：
   - 检测并安装 FFmpeg
   - 检测并安装 Python 依赖
   - 检测并安装 Whisper

3. **配置 API 密钥**
   安装完成后，运行以下命令配置 API：
   ```bash
   python scripts/configure.py
   ```

### 方法二：手动安装

如果您更喜欢手动安装，请按照以下步骤操作：

#### 1. 安装 FFmpeg

**Windows:**
```bash
# 使用 winget
winget install ffmpeg

# 或使用 chocolatey
choco install ffmpeg

# 或手动下载
# 1. 访问 https://ffmpeg.org/download.html
# 2. 下载 Windows 版本
# 3. 解压到 C:\ffmpeg
# 4. 将 C:\ffmpeg\bin 添加到系统 PATH
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

#### 2. 安装 Python 依赖

```bash
pip install -r scripts/requirements.txt
```

#### 3. 安装 Whisper

```bash
# 推荐使用 faster-whisper (更快)
pip install faster-whisper

# 或使用 openai-whisper
pip install openai-whisper
```

#### 4. 配置 API 密钥

创建配置文件：
```bash
# 创建配置目录
mkdir -p ~/.agents/config

# 创建配置文件
cat > ~/.agents/config/auto-video-skill-config.json << EOF
{
  "binghuo_api_key": "YOUR_BINGHUO_KEY",
  "xiaomi_api_key": "YOUR_XIAOMI_API_KEY",
  "agnes_api_key": "YOUR_AGNES_API_KEY"
}
EOF
```

## 🔧 验证安装

运行以下命令验证安装是否成功：

```bash
# 检查 FFmpeg
ffmpeg -version

# 检查 Python
python --version

# 检查 Whisper
python -c "import faster_whisper; print('faster-whisper OK')"

# 运行环境检查
python scripts/setup.py
```

## 🚀 使用 Skill

安装完成后，您可以通过以下方式使用 Skill：

### 在 DeepSeek Harness 中使用
```bash
/install-skill https://github.com/gigizhang0527-cmyk/auto-video-skill
```

### 直接运行脚本
```bash
# 运行完整流程
python scripts/run_workflow.py --input "您的文案.txt"

# 运行单个步骤
python scripts/generate_images.py --prompt "您的提示词"
```

## ❓ 常见问题

### Q: FFmpeg 安装失败怎么办？
A: 请手动下载 FFmpeg 并添加到系统 PATH。详见 [FFmpeg 官网](https://ffmpeg.org/download.html)。

### Q: Whisper 安装失败怎么办？
A: 请确保 Python 版本 >= 3.8，并尝试使用 `pip install --upgrade pip` 更新 pip。

### Q: API 调用失败怎么办？
A: 请检查：
1. API Key 是否正确
2. 网络连接是否正常
3. 账户余额是否充足

### Q: 如何更新 Skill？
A: 进入项目目录，运行：
```bash
git pull
pip install -r scripts/requirements.txt
```

## 📞 获取帮助

如果遇到问题，请：
1. 查看 [Issues](https://github.com/gigizhang0527-cmyk/auto-video-skill/issues)
2. 提交新的 Issue
3. 联系作者：[GitHub Profile](https://github.com/gigizhang0527-cmyk)

## 📜 许可证

MIT License
