#!/usr/bin/env python3
"""
自动视频创作 Skill - 一键安装脚本
用户只需运行此脚本，即可完成所有配置
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, check=True):
    """运行命令"""
    try:
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        return result.returncode == 0
    except:
        return False

def main():
    """主安装流程"""
    print("=" * 60)
    print("🎬 全自动视频创作 Skill - 一键安装")
    print("=" * 60)
    print()
    
    # 获取脚本目录
    script_dir = Path(__file__).parent
    
    # 1. 安装依赖
    print("📦 正在安装依赖...")
    if run_command(f"python {script_dir / 'setup.py'}"):
        print("✅ 依赖安装完成")
    else:
        print("⚠️  依赖安装可能有问题，但会继续...")
    
    print()
    
    # 2. 运行配置向导（安全版本）
    print("🔑 正在启动安全配置向导...")
    print("   向导会自动打开浏览器和记事本，请按照提示完成配置。")
    print("   ⚠️  API Key 将直接保存到本地文件，不会在聊天中显示。")
    print()
    
    if run_command(f"python {script_dir / 'onboarding.py'}", check=False):
        print("✅ 配置完成")
    else:
        print("⚠️  配置未完成，但您可以稍后运行：")
        print(f"   python {script_dir / 'onboarding.py'}")
    
    print()
    
    # 3. 检查配置
    print("🔍 正在检查配置...")
    if run_command(f"python {script_dir / 'check_config.py'}", check=False):
        print("✅ 配置检查通过")
    else:
        print("⚠️  配置检查未完全通过，请根据提示补充。")
    
    print()
    print("=" * 60)
    print("🎉 安装完成！")
    print()
    print("现在，您可以告诉 AI Agent：")
    print()
    print('  "帮我创作一个视频：[您的文案内容]"')
    print()
    print("Agent 会自动执行全流程，为您生成精彩的视频！")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
