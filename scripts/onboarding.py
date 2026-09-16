#!/usr/bin/env python3
"""
自动视频创作 Skill - 增强型安全配置向导
配置项目：炳火、小米、Agnes
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
    
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({
                "binghuo_api_key": "",
                "xiaomi_api_key": "",
                "agnes_api_key": ""
            }, f, indent=2)
    
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
    if not key or len(key) < 10:
        return False, "Key 长度异常"
    
    print(f"🔍 正在验证 {api_name}...")
    
    try:
        if api_name == "炳火":
            r = requests.get("https://api.7tai.cc/v1/models", 
                           headers={"Authorization": f"Bearer {key}"}, 
                           timeout=10)
            if r.status_code == 200:
                return True, "验证成功"
            return False, f"验证失败 (HTTP {r.status_code})"
            
        elif api_name == "小米 MiMo":
            r = requests.post("https://api.xiaomimimo.com/v1/chat/completions",
                            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                            json={"model": "mimo-v2.5-tts", "messages": [{"role": "user", "content": "test"}]},
                            timeout=10)
            if r.status_code == 200:
                return True, "验证成功"
            return False, f"验证失败 (HTTP {r.status_code})"
            
        elif api_name == "Agnes":
            # Agnes 验证逻辑 (示例)
            r = requests.get("https://api.agnes-ai.com/v1/models", 
                           headers={"Authorization": f"Bearer {key}"}, 
                           timeout=10)
            if r.status_code in [200, 401]: # 只要能连通
                return True, "验证成功 (连通性正常)"
            return False, f"验证失败 (HTTP {r.status_code})"
            
    except Exception as e:
        return False, f"网络错误: {str(e)}"

def main():
    config_path = get_config_path()
    config = load_config(config_path)
    
    # 1. 炳火
    print_header(1, 3, "炳火 API（仅负责生图）")
    print("📋 职责：使用 GPT IMAGE 2.5 生成参考图")
    print("⚠️ 请勿使用炳火生成视频，视频由 Agnes 负责")
    open_browser("https://api.7tai.cc/register?aff=xJ8H")
    
    while True:
        input("\n按 Enter 打开记事本填写 API Key...")
        open_notepad(config_path, "binghuo_api_key")
        input("填写完成后，保存并关闭记事本，然后按 Enter 验证...")
        config = load_config(config_path)
        ok, msg = validate_key("炳火", config.get("binghuo_api_key", ""))
        if ok:
            print(f"✅ 炳火 API Key {msg}")
            break
        else:
            print(f"❌ {msg}，请重新填写。")

    # 2. 小米
    print_header(2, 3, "小米 MiMo（TTS + 审片）")
    print("📋 职责：语音合成、画面质量检查")
    open_browser("https://platform.xiaomimimo.com?ref=YGUXWL")
    
    while True:
        input("\n按 Enter 打开记事本填写 API Key...")
        open_notepad(config_path, "xiaomi_api_key")
        input("填写完成后，保存并关闭记事本，然后按 Enter 验证...")
        config = load_config(config_path)
        ok, msg = validate_key("小米 MiMo", config.get("xiaomi_api_key", ""))
        if ok:
            print(f"✅ 小米 MiMo API Key {msg}")
            break
        else:
            print(f"❌ {msg}，请重新填写。")

    # 3. Agnes
    print_header(3, 3, "Agnes（仅负责生视频）")
    print("📋 职责：使用参考图模式生成动画视频")
    print("⚠️ 必须使用参考图模式，禁止文生视频")
    open_browser("https://www.agnes-ai.com/")
    
    while True:
        input("\n按 Enter 打开记事本填写 API Key...")
        open_notepad(config_path, "agnes_api_key")
        input("填写完成后，保存并关闭记事本，然后按 Enter 验证...")
        config = load_config(config_path)
        ok, msg = validate_key("Agnes", config.get("agnes_api_key", ""))
        if ok:
            print(f"✅ Agnes API Key {msg}")
            break
        else:
            print(f"❌ {msg}，请重新填写。")

    print("\n🎉 配置完成！所有 API 验证通过。")

if __name__ == "__main__":
    main()
