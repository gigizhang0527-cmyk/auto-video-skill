#!/usr/bin/env python3
"""
GitHub Image Uploader
Uses GitHub repository as image hosting to bypass SSL/Proxy issues.
"""

import os
import sys
import json
import base64
import requests
from pathlib import Path
from datetime import datetime

CONFIG_PATH = Path.home() / ".agents" / "config" / "auto-video-skill-config.json"
REPO_NAME = "auto-video-skill-assets" # 专门用来存图片的仓库

def get_github_token():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
            # 复用炳火或小米的 key 不合适，我们需要 github token
            # 这里假设用户会把 github token 也放进去，或者我们引导他放
            return config.get("github_token")
    return None

def upload_to_github(file_path, token):
    """
    上传文件到 GitHub 并返回 raw URL
    """
    if not token:
        return None, "GitHub Token 未配置"
        
    file_name = os.path.basename(file_path)
    date_str = datetime.now().strftime("%Y-%m-%d")
    repo_path = f"images/{date_str}/{file_name}"
    
    # 获取用户名
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    user_resp = requests.get("https://api.github.com/user", headers=headers)
    if user_resp.status_code != 200:
        return None, "GitHub Token 无效"
    
    username = user_resp.json()["login"]
    repo_full_name = f"{username}/{REPO_NAME}"
    
    # 确保仓库存在
    repo_resp = requests.get(f"https://api.github.com/repos/{repo_full_name}", headers=headers)
    if repo_resp.status_code == 404:
        # 创建仓库
        print(f"Creating repository {REPO_NAME}...")
        create_resp = requests.post("https://api.github.com/user/repos", headers=headers, json={
            "name": REPO_NAME,
            "description": "Auto Video Skill Assets",
            "auto_init": True
        })
        if create_resp.status_code not in [200, 201]:
            return None, f"创建仓库失败: {create_resp.text}"
    
    # 读取文件
    with open(file_path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")
        
    # 检查文件是否存在
    file_url = f"https://api.github.com/repos/{repo_full_name}/contents/{repo_path}"
    file_resp = requests.get(file_url, headers=headers)
    sha = file_resp.json().get("sha") if file_resp.status_code == 200 else None
    
    # 上传/更新文件
    payload = {
        "message": f"Upload {file_name}",
        "content": content
    }
    if sha:
        payload["sha"] = sha
        
    upload_resp = requests.put(file_url, headers=headers, json=payload)
    if upload_resp.status_code in [200, 201]:
        # 返回 raw url
        raw_url = f"https://raw.githubusercontent.com/{repo_full_name}/main/{repo_path}"
        return raw_url, None
    else:
        return None, f"上传失败: {upload_resp.status_code}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python github_uploader.py <image_path>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    token = get_github_token()
    
    if not token:
        print("ERROR: GitHub Token not found in config. Please add 'github_token' to config file.")
        sys.exit(1)
        
    print(f"Uploading {file_path} to GitHub...")
    url, err = upload_to_github(file_path, token)
    if url:
        print(f"SUCCESS: {url}")
    else:
        print(f"FAILED: {err}")
