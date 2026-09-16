#!/usr/bin/env python3
"""
自动视频创作 Skill - 交互式安全配置向导
自动打开浏览器和记事本，提供清晰的引导
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

def print_header(step, total, title):
    """打印步骤标题"""
    clear_screen()
    print("=" * 70)
    print(f"🎬 全自动视频创作 Skill - 配置向导")
    print(f"   步骤 {step}/{total}: {title}")
    print("=" * 70)
    print()

def wait_for_user(message="按 Enter 继续..."):
    """等待用户确认"""
    input(f"\n{message}")

def open_browser(url):
    """打开浏览器"""
    print(f"🌐 正在打开浏览器：{url}")
    webbrowser.open(url)
    time.sleep(3)  # 等待浏览器打开

def open_notepad(file_path, field_name, instructions):
    """打开记事本编辑文件，并提供清晰的填写说明"""
    print(f"📝 正在打开记事本：{file_path}")
    
    # 确保配置文件存在且包含基本结构
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({
                "binghuo_api_key": "",
                "xiaomi_api_key": "",
                "agnes_api_key": ""
            }, f, indent=2, ensure_ascii=False)
    
    if os.name == 'nt':  # Windows
        subprocess.Popen(['notepad.exe', str(file_path)])
    elif os.name == 'posix':  # macOS/Linux
        subprocess.Popen(['open', '-e', str(file_path)])
    
    time.sleep(2)  # 等待记事本打开
    
    print()
    print("=" * 70)
    print("📋 请在记事本中完成以下操作：")
    print("=" * 70)
    print()
    print(f"1. 找到字段：\"{field_name}\"")
    print(f"2. 将其值从 \"\" 改为您的 API Key")
    print(f"3. 例如：\"{field_name}\": \"your-api-key-here\"")
    print()
    print("⚠️  注意事项：")
    print("   - 保持 JSON 格式正确（保留引号和逗号）")
    print("   - 不要删除其他字段")
    print("   - 保存后关闭记事本")
    print()
    print("💡 提示：如果记事本为空，请等待几秒后重试。")
    print("=" * 70)

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
                content = f.read().strip()
                if not content:  # 文件为空
                    return {}
                return json.loads(content)
        except json.JSONDecodeError:
            print("⚠️  配置文件格式错误，将重新创建。")
            return {}
        except Exception as e:
            print(f"⚠️  读取配置文件失败: {e}")
            return {}
    return {}

def save_config(config_path, config):
    """保存配置文件"""
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ 保存配置文件失败: {e}")
        return False

def verify_field(config, field_name, platform_name):
    """验证字段是否已填写"""
    value = config.get(field_name, "").strip()
    if not value:
        return False, f"{platform_name} API Key 未填写"
    if value.startswith("YOUR_") or value == "":
        return False, f"{platform_name} API Key 仍为占位符"
    return True, f"{platform_name} API Key 已填写"

def main():
    """主引导流程"""
    config_path = get_config_path()
    
    # 初始化配置文件
    if not config_path.exists():
        save_config(config_path, {
            "binghuo_api_key": "",
            "xiaomi_api_key": "",
            "agnes_api_key": ""
        })
    
    config = load_config(config_path)
    
    # 步骤 1：炳火 API
    print_header(1, 3, "炳火 API（用于生图）")
    print("📋 炳火 API 提供 GPT IMAGE 2.5 模型，用于生成高质量参考图。")
    print()
    print("💰 价格参考：")
    print("  - 主价格表：https://mcn1eoufbabt.feishu.cn/wiki/D0XMwr2EXibFsQkd2Z0ctO5WnUg")
    print("  - 备用价格表：https://mcn1eoufbabt.feishu.cn/wiki/UWujw9W9yiXBLXkKHfacSabFnuc")
    print()
    print("⚠️  请使用您自己的飞书账号查看价格，不要使用他人的授权账号。")
    
    # 自动打开浏览器
    open_browser("https://api.7tai.cc/register?aff=xJ8H")
    
    print()
    print("👉 请在浏览器中完成注册，然后获取 API Key。")
    
    wait_for_user("注册完成后，按 Enter 打开记事本填写 API Key...")
    
    # 自动打开记事本
    open_notepad(config_path, "binghuo_api_key", "炳火 API Key")
    
    wait_for_user("填写完成后，保存并关闭记事本，然后按 Enter 继续...")
    
    # 验证填写
    config = load_config(config_path)
    ok, msg = verify_field(config, "binghuo_api_key", "炳火")
    if not ok:
        print(f"❌ {msg}")
        print("   请重新运行脚本并填写正确的 API Key。")
        return 1
    else:
        print(f"✅ {msg}")
    
    # 步骤 2：小米 MiMo
    print_header(2, 3, "小米 MiMo（用于审片 & TTS）")
    print("📋 小米 MiMo 提供：")
    print("  - 视觉审片：自动检查视频画面质量")
    print("  - TTS 语音合成：生成自然流畅的旁白")
    
    # 自动打开浏览器
    open_browser("https://platform.xiaomimimo.com?ref=YGUXWL")
    
    print()
    print("👉 请在浏览器中完成注册，然后获取 API Key。")
    
    wait_for_user("注册完成后，按 Enter 打开记事本填写 API Key...")
    
    # 自动打开记事本
    open_notepad(config_path, "xiaomi_api_key", "小米 MiMo API Key")
    
    wait_for_user("填写完成后，保存并关闭记事本，然后按 Enter 继续...")
    
    # 验证填写
    config = load_config(config_path)
    ok, msg = verify_field(config, "xiaomi_api_key", "小米 MiMo")
    if not ok:
        print(f"❌ {msg}")
        print("   请重新运行脚本并填写正确的 API Key。")
        return 1
    else:
        print(f"✅ {msg}")
    
    # 步骤 3：Agnes
    print_header(3, 3, "Agnes（用于视频生成）")
    print("📋 Agnes 是一款强大的 AI 视频生成工具，")
    print("   可以根据参考图和提示词生成高质量的动画视频。")
    
    # 自动打开浏览器
    open_browser("https://www.agnes-ai.com/")
    
    print()
    print("👉 请在浏览器中完成注册，然后获取 API Key。")
    
    wait_for_user("注册完成后，按 Enter 打开记事本填写 API Key...")
    
    # 自动打开记事本
    open_notepad(config_path, "agnes_api_key", "Agnes API Key")
    
    wait_for_user("填写完成后，保存并关闭记事本，然后按 Enter 继续...")
    
    # 验证填写
    config = load_config(config_path)
    ok, msg = verify_field(config, "agnes_api_key", "Agnes")
    if not ok:
        print(f"❌ {msg}")
        print("   请重新运行脚本并填写正确的 API Key。")
        return 1
    else:
        print(f"✅ {msg}")
    
    # 完成
    clear_screen()
    print("=" * 70)
    print("🎉 配置完成！")
    print("=" * 70)
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
    print("=" * 70)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
