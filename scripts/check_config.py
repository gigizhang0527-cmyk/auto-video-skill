#!/usr/bin/env python3
"""
自动视频创作 Skill - 配置检查脚本
运行前检查所有必要配置是否完整
"""

import os
import sys
import json
from pathlib import Path

def load_config():
    """加载配置文件"""
    config_paths = [
        Path.home() / ".agents" / "config" / "auto-video-skill-config.json",
        Path.cwd() / "config" / "auto-video-skill-config.json",
    ]
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    return json.load(f), config_path
            except Exception as e:
                pass
    
    return None, None

def check_api_key(key_name, key_value):
    """检查 API Key 是否有效"""
    if not key_value:
        return False, "未配置"
    
    if key_value.startswith("YOUR_"):
        return False, "未填写（仍为占位符）"
    
    if len(key_value) < 10:
        return False, "长度异常（可能不完整）"
    
    return True, "✅ 已配置"

def check_ffmpeg():
    """检查 FFmpeg 是否可用"""
    import shutil
    if shutil.which("ffmpeg"):
        return True, "✅ 已安装"
    return False, "未安装"

def check_whisper():
    """检查 Whisper 是否可用"""
    try:
        import faster_whisper
        return True, "✅ 已安装"
    except ImportError:
        pass
    
    try:
        import whisper
        return True, "✅ 已安装"
    except ImportError:
        pass
    
    return False, "未安装"

def main():
    """主检查流程"""
    print("=" * 60)
    print("🔍 自动视频创作 Skill - 配置检查")
    print("=" * 60)
    print()
    
    all_ok = True
    
    # 检查配置文件
    config, config_path = load_config()
    if config:
        print(f"📁 配置文件：{config_path}")
    else:
        print("❌ 未找到配置文件，请先运行配置向导")
        print("   python scripts/onboarding.py")
        return 1
    
    print()
    print("📋 API 配置检查：")
    print("-" * 40)
    
    # 检查炳火 API
    ok, status = check_api_key("炳火 API", config.get("binghuo_api_key"))
    print(f"  炳火 API (生图)：{status}")
    if not ok:
        all_ok = False
        print(f"    → 注册链接：https://api.7tai.cc/register?aff=xJ8H")
    
    # 检查小米 MiMo
    ok, status = check_api_key("小米 MiMo", config.get("xiaomi_api_key"))
    print(f"  小米 MiMo (审片 & TTS)：{status}")
    if not ok:
        all_ok = False
        print(f"    → 注册链接：https://platform.xiaomimimo.com?ref=YGUXWL")
    
    # 检查 Agnes
    ok, status = check_api_key("Agnes", config.get("agnes_api_key"))
    print(f"  Agnes (视频生成)：{status}")
    if not ok:
        all_ok = False
        print(f"    → 注册链接：https://www.agnes-ai.com/")
    
    print()
    print("🛠️  环境检查：")
    print("-" * 40)
    
    # 检查 FFmpeg
    ok, status = check_ffmpeg()
    print(f"  FFmpeg (视频处理)：{status}")
    if not ok:
        all_ok = False
        print(f"    → 安装命令：python scripts/setup.py")
    
    # 检查 Whisper
    ok, status = check_whisper()
    print(f"  Whisper (语音识别)：{status}")
    if not ok:
        all_ok = False
        print(f"    → 安装命令：pip install faster-whisper")
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("✅ 所有检查通过！可以开始创作视频了。")
        print()
        print("使用方法：")
        print('  python scripts/run_workflow.py --input "您的文案.txt"')
        print()
        print("或告诉 AI Agent：")
        print('  "帮我创作一个视频：[您的文案内容]"')
        return 0
    else:
        print("⚠️  部分检查未通过，请根据上述提示完成配置。")
        print()
        print("快速配置：")
        print("  python scripts/onboarding.py")
        return 1

if __name__ == "__main__":
    sys.exit(main())
