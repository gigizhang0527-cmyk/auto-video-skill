#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Image Hosting Service Test Script
Tests multiple free image hosting services to find one accessible by Agnes.
"""

import requests
import base64
import time
import os
from PIL import Image
import io
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_test_image():
    """Create a test image"""
    img = Image.new('RGB', (100, 100), color = 'red')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

def test_catbox(image_data):
    """Test catbox.moe"""
    print("Testing catbox.moe...")
    try:
        files = {'fileToUpload': ('test.png', image_data, 'image/png')}
        data = {'reqtype': 'fileupload'}
        r = requests.post("https://catbox.moe/user/api.php", files=files, data=data, timeout=30, verify=False)
        if r.status_code == 200 and r.text.startswith("http"):
            return r.text.strip(), "catbox"
    except Exception as e:
        print(f"   Failed: {e}")
    return None, None

def test_telegraph(image_data):
    """Test telegra.ph"""
    print("Testing telegra.ph...")
    try:
        files = {'file': ('test.png', image_data, 'image/png')}
        r = requests.post("https://telegra.ph/upload", files=files, timeout=30, verify=False)
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, list) and len(data) > 0:
                src = data[0].get('src')
                if src:
                    return f"https://telegra.ph{src}", "telegraph"
    except Exception as e:
        print(f"   Failed: {e}")
    return None, None

def test_0x0(image_data):
    """Test 0x0.st"""
    print("Testing 0x0.st...")
    try:
        files = {'file': ('test.png', image_data, 'image/png')}
        r = requests.post("https://0x0.st", files=files, timeout=30, verify=False)
        if r.status_code == 200:
            return r.text.strip(), "0x0"
    except Exception as e:
        print(f"   Failed: {e}")
    return None, None

def test_smms(image_data):
    """Test sm.ms"""
    print("Testing sm.ms...")
    try:
        files = {'smfile': ('test.png', image_data, 'image/png')}
        r = requests.post("https://sm.ms/api/v2/upload", files=files, timeout=30, verify=False)
        if r.status_code == 200:
            data = r.json()
            if data.get('success'):
                return data['data']['url'], "smms"
    except Exception as e:
        print(f"   Failed: {e}")
    return None, None

def test_agnes_access(url):
    """Test if Agnes can access the URL"""
    print(f"   Testing Agnes access: {url}")
    try:
        # Simulate Agnes request
        r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        content_type = r.headers.get('Content-Type', '')
        
        if 'image' in content_type:
            print(f"   OK: Accessible (Content-Type: {content_type})")
            return True
        elif r.status_code == 200:
            print(f"   Warning: 200 OK but not image (Content-Type: {content_type})")
            return False
        else:
            print(f"   Fail: HTTP {r.status_code}")
            return False
    except Exception as e:
        print(f"   Fail: {e}")
        return False

def main():
    print("=" * 60)
    print("Image Hosting Service Test")
    print("=" * 60)
    
    # Create test image
    image_data = create_test_image()
    print(f"Test image created ({len(image_data)} bytes)")
    print()
    
    # Test each service
    services = [
        ("catbox", test_catbox),
        ("telegraph", test_telegraph),
        ("0x0", test_0x0),
        ("smms", test_smms),
    ]
    
    results = []
    
    for name, test_func in services:
        url, service = test_func(image_data)
        if url:
            print(f"   Upload success: {url}")
            # Test if Agnes can access
            accessible = test_agnes_access(url)
            results.append((service, url, accessible))
        else:
            print(f"   Upload failed")
        print()
        time.sleep(1)  # Avoid rate limiting
    
    # Summary
    print("=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    for service, url, accessible in results:
        status = "OK: Agnes Accessible" if accessible else "FAIL: Agnes Cannot Access"
        print(f"{service}: {status}")
        print(f"   URL: {url}")
    
    # Recommendation
    print()
    print("Recommendation:")
    accessible_services = [s for s, _, a in results if a]
    if accessible_services:
        print(f"   Use {accessible_services[0]}")
    else:
        print("   All image hosts are inaccessible to Agnes, consider base64 or self-hosting")

if __name__ == "__main__":
    main()
