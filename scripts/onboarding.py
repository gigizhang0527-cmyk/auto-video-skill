#!/usr/bin/env python3
"""
自动视频创作 Skill - 增强型安全配置向导
特性：
1. 逐步引导（炳火 -> 小米）
2. 自动打开浏览器
3. 填写后立即验证 API Key 有效性
4. 验证失败不允许进入下一步
5. 移除 Agnes，统一使用炳火 API
"""

import os
import sys
import json
import time
import subprocess
import webbrowser
import requests
from pathlib import Path

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(step, total, title):
    clear_screen()
    print("=" * 70)
    print(f"🎬 全自动视频创作 Skill - 配置向导")
    print(f"   步骤 {step}/{total}: {title}")
    print("=" * 70)
    print()

def open_browser(url):
    print(f"🌐 正在打开浏览器：{url}")
    webbrowser.open(url)
    time.sleep(2)

def open_notepad(file_path, field_name):
    print(f"📝 正在打开记事本：{file_path}")
    
    # 确保 JSON 结构存在
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({"binghuo_api_key": "", "xiaomi_api_key": ""}, f, indent=2)
    
    if os.name == 'nt':
        subprocess.Popen(['notepad.exe', str(file_path)])
    elif os.name == 'posix':
        subprocess.Popen(['open', '-e', str(file_path)])
    
    print()
    print("👉 请在记事本中完成以下操作：")
    print(f"   1. 找到 \"{field_name}\"")
    print(f"   2. 填入您的 API Key (保留引号)")
    print(f"   3. 保存 (Ctrl+S) 并关闭记事本")

def get_config_path():
    return Path.home() / ".agents" / "config" / "auto-video-skill-config.json"

def load_config(path):
    if path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def validate_key(api_name, key):
    """验证 API Key 是否有效"""
    if not key or len(key) < 10:
        return False, "Key 长度异常"
    
    print(f"🔍 正在验证 {api_name}...")
    
    try:
        if api_name == "炳火":
            # 测试炳火 API
            r = requests.get("https://api.7tai.cc/v1/models", 
                           headers={"Authorization": f"Bearer {key}"}, 
                           timeout=10)
            if r.status_code == 200:
                return True, "验证成功"
            return False, f"验证失败 (HTTP {r.status_code})"
            
        elif api_name == "小米 MiMo":
            # 测试小米 TTS API
            r = requests.post("https://api.xiaomimimo.com/v1/chat/completions",
                            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                            json={"model": "mimo-v2.5-tts", "messages": [{"role": "user", "content": "test"}]},
                            timeout=10)
            if r.status_code == 200:
                return True, "验证成功"
            return False, f"验证失败 (HTTP {r.status_code})"
            
    except Exception as e:
        return False, f"网络错误: {str(e)}"

def main():
    config_path = get_config_path()
    config = load_config(config_path)
    
    # 步骤 1：炳火 API
    print_header(1, 2, "炳火 API（生图 + 视频生成）")
    print("📋 炳火 API 提供：")
    print("  - GPT IMAGE 2.5：高质量参考图生成")
    print("  - Seedance：AI 视频生成")
    print()
    print("💰 价格参考（飞书文档）：")
    print("  - https://mcn1eoufbabt.feishu.cn/wiki/D0XMwr2EXibFsQkd2Z0ctO5WnUg")
    
    open_browser("https://api.7tai.cc/register?aff=xJ8H")
    
    while True:
        input("\n按 Enter 打开记事本填写 API Key...")
        open_notepad(config_path, "binghuo_api_key")
        
        input("填写完成后，保存并关闭记事本，然后按 Enter 验证...")
        
        config = load_config(config_path)
        key = config.get("binghuo_api_key", "")
        
        ok, msg = validate_key("炳火", key)
        if ok:
            print(f"✅ 炳火 API Key {msg}")
            break
        else:
            print(f"❌ {msg}，请重新填写。")

    # 步骤 2：小米 MiMo
    print_header(2, 2, "小米 MiMo（审片 + TTS）")
    print("📋 小米 MiMo 提供：")
    print("  - 视觉审片：自动检查画面质量")
    print("  - TTS 语音：生成自然流畅的旁白")
    
    open_browser("https://platform.xiaomimimo.com?ref=YGUXWL")
    
    while True:
        input("\n按 Enter 打开记事本填写 API Key...")
        open_notepad(config_path, "xiaomi_api_key")
        
        input("填写完成后，保存并关闭记事本，然后按 Enter 验证...")
        
        config = load_config(config_path)
        key = config.get("xiaomi_api_key", "")
        
        ok, msg = validate_key("小米 MiMo", key)
        if ok:
            print(f"✅ 小米 MiMo API Key {msg}")
            break
        else:
            print(f"❌ {msg}，请重新填写。")

    # 完成
    clear_screen()
    print("=" * 70)
    print("🎉 配置完成！所有 API 验证通过。")
    print("=" * 70)
    print()
    print("现在您可以告诉我：")
    print('  "帮我创作一个视频：[您的文案内容]"')
    print()

if __name__ == "__main__":
    main()
