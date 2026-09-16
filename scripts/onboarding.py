#!/usr/bin/env python3
"""
自动视频创作 Skill - 安全的用户引导脚本
自动打开浏览器和记事本，避免在聊天框中输入 API Key
"""

import os
import sys
import json
import time
import subprocess
import webbrowser
from pathlib import Path

def clear_screen():
    """清屏"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(step, total):
    """打印步骤标题"""
    clear_screen()
    print("=" * 60)
    print(f"🎬 全自动视频创作 Skill - 配置向导")
    print(f"   步骤 {step}/{total}")
    print("=" * 60)
    print()

def wait_for_user():
    """等待用户确认"""
    input("\n按 Enter 继续...")

def open_browser(url):
    """打开浏览器"""
    print(f"🌐 正在打开浏览器：{url}")
    webbrowser.open(url)
    time.sleep(2)  # 等待浏览器打开

def open_notepad(file_path):
    """打开记事本编辑文件"""
    print(f"📝 正在打开记事本：{file_path}")
    if os.name == 'nt':  # Windows
        subprocess.Popen(['notepad.exe', str(file_path)])
    elif os.name == 'posix':  # macOS/Linux
        subprocess.Popen(['open', '-e', str(file_path)])
    time.sleep(2)  # 等待记事本打开

def get_config_path():
    """获取配置文件路径"""
    config_dir = Path.home() / ".agents" / "config"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / "auto-video-skill-config.json"

def load_config(config_path):
    """加载配置文件"""
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {}

def save_config(config_path, config):
    """保存配置文件"""
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def main():
    """主引导流程"""
    config_path = get_config_path()
    config = load_config(config_path)
    
    # 步骤 1：炳火 API
    print_header(1, 3)
    print("📋 第一步：注册炳火 API（用于生图）")
    print()
    print("炳火 API 提供 GPT IMAGE 2.5 模型，用于生成高质量参考图。")
    print()
    print("价格参考：")
    print("  - 主价格表：https://mcn1eoufbabt.feishu.cn/wiki/D0XMwr2EXibFsQkd2Z0ctO5WnUg")
    print("  - 备用价格表：https://mcn1eoufbabt.feishu.cn/wiki/UWujw9W9yiXBLXkKHfacSabFnuc")
    print()
    print("⚠️  请使用您自己的飞书账号查看价格，不要使用他人的授权账号。")
    print()
    
    # 自动打开浏览器
    open_browser("https://api.7tai.cc/register?aff=xJ8H")
    
    print()
    print("请在浏览器中完成注册，然后获取 API Key。")
    print()
    print("获取 API Key 后，请在记事本中填写。")
    print()
    
    # 自动打开记事本
    save_config(config_path, config)  # 先保存当前配置
    open_notepad(config_path)
    
    print()
    print("请在记事本中找到 \"binghuo_api_key\" 字段，")
    print("将您的 API Key 填写进去，然后保存并关闭记事本。")
    print()
    print("完成后，请回到这里按 Enter 继续...")
    wait_for_user()
    
    # 重新加载配置
    config = load_config(config_path)
    
    # 步骤 2：小米 MiMo
    print_header(2, 3)
    print("📋 第二步：注册小米 MiMo（用于审片 & TTS）")
    print()
    print("小米 MiMo 提供：")
    print("  - 视觉审片：自动检查视频画面质量")
    print("  - TTS 语音合成：生成自然流畅的旁白")
    print()
    
    # 自动打开浏览器
    open_browser("https://platform.xiaomimimo.com?ref=YGUXWL")
    
    print()
    print("请在浏览器中完成注册，然后获取 API Key。")
    print()
    print("获取 API Key 后，请在记事本中填写。")
    print()
    
    # 自动打开记事本
    open_notepad(config_path)
    
    print()
    print("请在记事本中找到 \"xiaomi_api_key\" 字段，")
    print("将您的 API Key 填写进去，然后保存并关闭记事本。")
    print()
    print("完成后，请回到这里按 Enter 继续...")
    wait_for_user()
    
    # 重新加载配置
    config = load_config(config_path)
    
    # 步骤 3：Agnes
    print_header(3, 3)
    print("📋 第三步：注册 Agnes（用于视频生成）")
    print()
    print("Agnes 是一款强大的 AI 视频生成工具，")
    print("可以根据参考图和提示词生成高质量的动画视频。")
    print()
    
    # 自动打开浏览器
    open_browser("https://www.agnes-ai.com/")
    
    print()
    print("请在浏览器中完成注册，然后获取 API Key。")
    print()
    print("获取 API Key 后，请在记事本中填写。")
    print()
    
    # 自动打开记事本
    open_notepad(config_path)
    
    print()
    print("请在记事本中找到 \"agnes_api_key\" 字段，")
    print("将您的 API Key 填写进去，然后保存并关闭记事本。")
    print()
    print("完成后，请回到这里按 Enter 继续...")
    wait_for_user()
    
    # 重新加载配置
    config = load_config(config_path)
    
    # 完成
    clear_screen()
    print("=" * 60)
    print("🎉 配置完成！")
    print("=" * 60)
    print()
    print("您已成功配置所有 API：")
    print(f"  ✅ 炳火 API：{config.get('binghuo_api_key', 'N/A')[:10]}...")
    print(f"  ✅ 小米 MiMo：{config.get('xiaomi_api_key', 'N/A')[:10]}...")
    print(f"  ✅ Agnes：{config.get('agnes_api_key', 'N/A')[:10]}...")
    print()
    print("现在，您可以告诉 AI Agent：")
    print()
    print('  "帮我创作一个视频：[您的文案内容]"')
    print()
    print("Agent 会自动执行全流程，为您生成精彩的视频！")
    print()
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
