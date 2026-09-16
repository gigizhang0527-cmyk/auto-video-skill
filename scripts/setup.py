#!/usr/bin/env python3
"""
自动视频创作 Skill - 环境安装脚本
自动检测并安装所需依赖：FFmpeg, Python, Whisper
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def run_command(cmd, check=True, shell=True):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=shell, check=check, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr
    except Exception as e:
        return False, "", str(e)

def check_ffmpeg():
    """检查 FFmpeg 是否已安装"""
    print("🔍 检查 FFmpeg...")
    
    # 检查是否在 PATH 中
    if shutil.which("ffmpeg"):
        print("✅ FFmpeg 已安装")
        return True
    
    # 检查常见安装路径
    common_paths = [
        r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
        os.path.expanduser(r"~\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"),
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            print(f"✅ FFmpeg 找到: {path}")
            # 添加到 PATH
            ffmpeg_dir = os.path.dirname(path)
            if ffmpeg_dir not in os.environ["PATH"]:
                os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]
            return True
    
    print("❌ FFmpeg 未安装")
    return False

def install_ffmpeg():
    """安装 FFmpeg"""
    print("📦 正在安装 FFmpeg...")
    
    system = platform.system().lower()
    
    if system == "windows":
        # 使用 winget 安装
        print("尝试使用 winget 安装 FFmpeg...")
        success, stdout, stderr = run_command("winget install ffmpeg", check=False)
        if success:
            print("✅ FFmpeg 安装成功")
            return True
        
        # 使用 chocolatey 安装
        print("尝试使用 chocolatey 安装 FFmpeg...")
        success, stdout, stderr = run_command("choco install ffmpeg", check=False)
        if success:
            print("✅ FFmpeg 安装成功")
            return True
        
        # 手动下载
        print("⚠️ 自动安装失败，请手动安装 FFmpeg:")
        print("   1. 访问 https://ffmpeg.org/download.html")
        print("   2. 下载 Windows 版本")
        print("   3. 解压到 C:\\ffmpeg")
        print("   4. 将 C:\\ffmpeg\\bin 添加到系统 PATH")
        return False
    
    elif system == "darwin":  # macOS
        # 使用 homebrew 安装
        print("尝试使用 homebrew 安装 FFmpeg...")
        success, stdout, stderr = run_command("brew install ffmpeg", check=False)
        if success:
            print("✅ FFmpeg 安装成功")
            return True
    
    elif system == "linux":
        # 使用 apt 安装
        print("尝试使用 apt 安装 FFmpeg...")
        success, stdout, stderr = run_command("sudo apt-get update && sudo apt-get install -y ffmpeg", check=False)
        if success:
            print("✅ FFmpeg 安装成功")
            return True
        
        # 使用 yum 安装
        print("尝试使用 yum 安装 FFmpeg...")
        success, stdout, stderr = run_command("sudo yum install -y ffmpeg", check=False)
        if success:
            print("✅ FFmpeg 安装成功")
            return True
    
    print("❌ FFmpeg 安装失败")
    return False

def check_python():
    """检查 Python 是否已安装"""
    print("🔍 检查 Python...")
    
    # 检查 Python 版本
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            print(f"✅ Python {version.major}.{version.minor}.{version.micro} 已安装")
            return True
        else:
            print(f"⚠️ Python 版本过低: {version.major}.{version.minor}.{version.micro}，需要 3.8+")
            return False
    except:
        print("❌ Python 未安装")
        return False

def check_whisper():
    """检查 Whisper 是否已安装"""
    print("🔍 检查 Whisper...")
    
    # 检查 faster-whisper
    try:
        import faster_whisper
        print("✅ faster-whisper 已安装")
        return True
    except ImportError:
        pass
    
    # 检查 openai-whisper
    try:
        import whisper
        print("✅ openai-whisper 已安装")
        return True
    except ImportError:
        pass
    
    print("❌ Whisper 未安装")
    return False

def install_whisper():
    """安装 Whisper"""
    print("📦 正在安装 Whisper...")
    
    # 安装 faster-whisper (更快)
    print("安装 faster-whisper...")
    success, stdout, stderr = run_command("pip install faster-whisper", check=False)
    if success:
        print("✅ faster-whisper 安装成功")
        return True
    
    # 安装 openai-whisper
    print("安装 openai-whisper...")
    success, stdout, stderr = run_command("pip install openai-whisper", check=False)
    if success:
        print("✅ openai-whisper 安装成功")
        return True
    
    print("❌ Whisper 安装失败")
    return False

def install_requirements():
    """安装 Python 依赖"""
    print("📦 正在安装 Python 依赖...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    if requirements_file.exists():
        success, stdout, stderr = run_command(f"pip install -r {requirements_file}", check=False)
        if success:
            print("✅ Python 依赖安装成功")
            return True
        else:
            print(f"⚠️ Python 依赖安装失败: {stderr}")
            return False
    else:
        print("⚠️ requirements.txt 不存在，跳过依赖安装")
        return True

def main():
    """主安装流程"""
    print("=" * 60)
    print("🎬 自动视频创作 Skill - 环境安装")
    print("=" * 60)
    print()
    
    success = True
    
    # 检查并安装 FFmpeg
    if not check_ffmpeg():
        if not install_ffmpeg():
            success = False
    
    # 检查 Python
    if not check_python():
        print("⚠️ 请手动安装 Python 3.8+")
        success = False
    
    # 检查并安装 Whisper
    if not check_whisper():
        if not install_whisper():
            success = False
    
    # 安装 Python 依赖
    if not install_requirements():
        success = False
    
    print()
    print("=" * 60)
    if success:
        print("✅ 环境检查完成！所有依赖已就绪。")
        print("   现在可以运行 auto-video-skill 了。")
    else:
        print("⚠️ 环境检查完成，但存在一些问题。")
        print("   请根据上述提示手动安装缺失的依赖。")
    print("=" * 60)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
