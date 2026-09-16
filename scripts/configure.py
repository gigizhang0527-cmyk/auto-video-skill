#!/usr/bin/env python3
"""
自动视频创作 Skill - API 配置脚本
引导用户配置所需的 API 密钥
"""

import os
import sys
import json
from pathlib import Path

def get_config_path():
    """获取配置文件路径"""
    # 优先使用用户目录下的配置
    home = Path.home()
    config_dir = home / ".agents" / "config"
    config_file = config_dir / "auto-video-skill-config.json"
    
    # 如果用户目录不存在，使用当前目录
    if not config_dir.exists():
        config_dir = Path.cwd() / "config"
        config_file = config_dir / "auto-video-skill-config.json"
    
    return config_file

def load_config(config_path):
    """加载配置文件"""
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ 读取配置文件失败: {e}")
    
    return {}

def save_config(config_path, config):
    """保存配置文件"""
    try:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"✅ 配置已保存到: {config_path}")
        return True
    except Exception as e:
        print(f"❌ 保存配置文件失败: {e}")
        return False

def prompt_api_key(name, description, current_value=None):
    """提示用户输入 API Key"""
    print(f"\n{'='*60}")
    print(f"🔑 配置 {name}")
    print(f"{'='*60}")
    print(f"说明: {description}")
    
    if current_value:
        print(f"当前值: {current_value[:10]}...{current_value[-10:]}")
        use_current = input("是否使用当前值？(y/n): ").strip().lower()
        if use_current == 'y':
            return current_value
    
    api_key = input(f"请输入 {name} API Key: ").strip()
    return api_key

def main():
    """主配置流程"""
    print("=" * 60)
    print("🎬 自动视频创作 Skill - API 配置")
    print("=" * 60)
    
    # 获取配置路径
    config_path = get_config_path()
    print(f"配置文件位置: {config_path}")
    
    # 加载现有配置
    config = load_config(config_path)
    
    # 配置炳火 API
    config["binghuo_api_key"] = prompt_api_key(
        "炳火 API",
        "用于生图 (GPT IMAGE 2.5)\n"
        "注册链接: https://api.7tai.cc/register?aff=xJ8H\n"
        "价格参考: https://mcn1eoufbabt.feishu.cn/wiki/D0XMwr2EXibFsQkd2Z0ctO5WnUg",
        config.get("binghuo_api_key")
    )
    
    # 配置小米 API
    config["xiaomi_api_key"] = prompt_api_key(
        "小米 MiMo API",
        "用于视觉审片和 TTS\n"
        "管理链接: https://platform.xiaomimimo.com/console/api-keys",
        config.get("xiaomi_api_key")
    )
    
    # 配置 Agnes API
    config["agnes_api_key"] = prompt_api_key(
        "Agnes API",
        "用于视频生成\n"
        "官网: https://www.agnes-ai.com/",
        config.get("agnes_api_key")
    )
    
    # 保存配置
    if save_config(config_path, config):
        print("\n" + "=" * 60)
        print("✅ 配置完成！")
        print("   现在可以运行 auto-video-skill 了。")
        print("=" * 60)
        return 0
    else:
        print("\n" + "=" * 60)
        print("❌ 配置失败！")
        print("   请检查权限或手动创建配置文件。")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
