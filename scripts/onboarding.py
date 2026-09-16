#!/usr/bin/env python3
"""
自动视频创作 Skill - 用户引导脚本
逐步引导用户完成 API 配置
"""

import os
import sys
import json
import time
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

def open_url(url):
    """打开浏览器"""
    import webbrowser
    webbrowser.open(url)
    print(f"✅ 已打开浏览器：{url}")

def get_api_key(platform_name):
    """获取 API Key"""
    print(f"\n请将您在 {platform_name} 获取的 API Key 粘贴到这里：")
    api_key = input("> ").strip()
    return api_key

def save_config(config):
    """保存配置"""
    config_dir = Path.home() / ".agents" / "config"
    config_dir.mkdir(parents=True, exist_ok=True)
    config_file = config_dir / "auto-video-skill-config.json"
    
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 配置已保存到：{config_file}")
    return config_file

def main():
    """主引导流程"""
    config = {}
    
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
    
    input("按 Enter 打开注册页面...")
    open_url("https://api.7tai.cc/register?aff=xJ8H")
    
    print()
    print("请在浏览器中完成注册，然后获取 API Key。")
    config["binghuo_api_key"] = get_api_key("炳火")
    save_config(config)
    wait_for_user()
    
    # 步骤 2：小米 MiMo
    print_header(2, 3)
    print("📋 第二步：注册小米 MiMo（用于审片 & TTS）")
    print()
    print("小米 MiMo 提供：")
    print("  - 视觉审片：自动检查视频画面质量")
    print("  - TTS 语音合成：生成自然流畅的旁白")
    print()
    
    input("按 Enter 打开注册页面...")
    open_url("https://platform.xiaomimimo.com?ref=YGUXWL")
    
    print()
    print("请在浏览器中完成注册，然后获取 API Key。")
    config["xiaomi_api_key"] = get_api_key("小米 MiMo")
    save_config(config)
    wait_for_user()
    
    # 步骤 3：Agnes
    print_header(3, 3)
    print("📋 第三步：注册 Agnes（用于视频生成）")
    print()
    print("Agnes 是一款强大的 AI 视频生成工具，")
    print("可以根据参考图和提示词生成高质量的动画视频。")
    print()
    
    input("按 Enter 打开注册页面...")
    open_url("https://www.agnes-ai.com/")
    
    print()
    print("请在浏览器中完成注册，然后获取 API Key。")
    config["agnes_api_key"] = get_api_key("Agnes")
    save_config(config)
    wait_for_user()
    
    # 完成
    clear_screen()
    print("=" * 60)
    print("🎉 配置完成！")
    print("=" * 60)
    print()
    print("您已成功配置所有 API：")
    print(f"  ✅ 炳火 API：{config['binghuo_api_key'][:10]}...")
    print(f"  ✅ 小米 MiMo：{config['xiaomi_api_key'][:10]}...")
    print(f"  ✅ Agnes：{config['agnes_api_key'][:10]}...")
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
