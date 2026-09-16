#!/usr/bin/env python3
"""
工具函数：图片上传
使用 catbox.moe (免费, 无需 API Key, 永久存储)
"""

import requests
import os

def upload_image_to_catbox(file_path):
    """
    将本地图片上传到 catbox.moe 并返回 URL。
    优点：免费，无需注册，永久存储，支持直接链接。
    """
    if not os.path.exists(file_path):
        return None, "文件不存在"

    url = "https://catbox.moe/user/api.php"
    
    try:
        with open(file_path, 'rb') as f:
            # reqtype=fileupload 是固定的
            files = {'fileToUpload': (os.path.basename(file_path), f)}
            data = {'reqtype': 'fileupload'}
            
            response = requests.post(url, files=files, data=data, timeout=30)
            
            if response.status_code == 200 and response.text.startswith("http"):
                return response.text.strip(), None
            else:
                return None, f"上传失败: {response.text}"
    except Exception as e:
        return None, f"上传异常: {str(e)}"

def upload_image_to_telegraph(file_path):
    """
    备用方案：上传到 Telegraph (Telegram 的图床)
    """
    url = "https://telegra.ph/upload"
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f)}
            response = requests.post(url, files=files, timeout=30)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    src = data[0].get('src')
                    if src:
                        return f"https://telegra.ph{src}", None
        return None, "Telegraph 上传失败"
    except Exception as e:
        return None, f"Telegraph 异常: {str(e)}"

if __name__ == "__main__":
    # 测试
    import sys
    if len(sys.argv) > 1:
        test_file = sys.argv[1]
        print(f"正在上传 {test_file}...")
        url, err = upload_image_to_catbox(test_file)
        if url:
            print(f"✅ 上传成功: {url}")
        else:
            print(f"❌ 失败: {err}")
