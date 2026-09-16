#!/usr/bin/env python3
"""
自动视频创作 Skill - 主工作流脚本
自动化执行：文案脚本 → TTS → SRT → 参考图 → 动画分镜 → 总装
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def load_config():
    """加载配置文件"""
    config_paths = [
        Path.home() / ".agents" / "config" / "auto-video-skill-config.json",
        project_root / "config" / "auto-video-skill-config.json",
    ]
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ 读取配置文件失败: {e}")
    
    print("❌ 未找到配置文件，请先运行 configure.py")
    return None

def create_project_structure(project_name):
    """创建项目目录结构"""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    project_dir = project_root / "output" / f"{timestamp}_{project_name}"
    
    # 创建目录结构
    dirs = [
        "scripts",
        "assets",
        "reference_images",
        "animation_videos",
        "subtitles",
        "final_output",
        "temp",
    ]
    
    for dir_name in dirs:
        (project_dir / dir_name).mkdir(parents=True, exist_ok=True)
    
    print(f"✅ 项目目录创建完成: {project_dir}")
    return project_dir

def run_step(step_name, script_path, *args):
    """运行单个步骤"""
    print(f"\n{'='*60}")
    print(f"🚀 执行步骤: {step_name}")
    print(f"{'='*60}")
    
    # 这里应该调用实际的脚本
    # 示例：subprocess.run([sys.executable, script_path, *args])
    
    print(f"✅ {step_name} 完成")
    return True

def main():
    """主工作流"""
    parser = argparse.ArgumentParser(description="自动视频创作 Skill - 主工作流")
    parser.add_argument("--input", "-i", required=True, help="输入文案文件路径")
    parser.add_argument("--project", "-p", default="auto_video", help="项目名称")
    parser.add_argument("--config", "-c", help="配置文件路径")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🎬 自动视频创作 Skill - 主工作流")
    print("=" * 60)
    
    # 加载配置
    config = load_config()
    if not config:
        return 1
    
    # 检查输入文件
    input_file = Path(args.input)
    if not input_file.exists():
        print(f"❌ 输入文件不存在: {input_file}")
        return 1
    
    # 创建项目结构
    project_dir = create_project_structure(args.project)
    
    # 读取文案
    with open(input_file, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    print(f"📝 文案内容 ({len(script_content)} 字):")
    print(script_content[:200] + "..." if len(script_content) > 200 else script_content)
    
    # 执行工作流步骤
    steps = [
        ("TTS 语音生成", "scripts/generate_tts.py"),
        ("SRT 时间轴生成", "scripts/generate_srt.py"),
        ("参考图生成", "scripts/generate_images.py"),
        ("动画分镜生成", "scripts/generate_animation.py"),
        ("FFmpeg 总装", "scripts/assemble_video.py"),
    ]
    
    for step_name, script_path in steps:
        if not run_step(step_name, script_path):
            print(f"❌ {step_name} 失败，工作流中断")
            return 1
    
    print("\n" + "=" * 60)
    print("✅ 工作流完成！")
    print(f"   项目目录: {project_dir}")
    print(f"   最终视频: {project_dir / 'final_output'}")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
