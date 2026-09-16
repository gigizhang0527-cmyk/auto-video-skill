# 🔑 API 配置指南

本 Skill 依赖以下 API 服务。请在使用前完成配置。

## 1. 炳火 API (BingHuo)
*   **用途**：生图 (GPT IMAGE 2.5)
*   **注册链接**：[点击注册 (使用推荐码)](https://api.7tai.cc/register?aff=xJ8H)
*   **价格参考**：
    *   [主价格表 (飞书)](https://mcn1eoufbabt.feishu.cn/wiki/D0XMwr2EXibFsQkd2Z0ctO5WnUg)
    *   [备用价格表 (飞书)](https://mcn1eoufbabt.feishu.cn/wiki/UWujw9W9yiXBLXkKHfacSabFnuc)
    *   **注意**：请使用您自己的飞书账号查看，不要使用他人的授权账号。
*   **获取 API Key**：登录后在「个人中心」获取 API Key。

## 2. 小米开放平台 (MiMo & TTS)
*   **用途**：视频画面质量检查 (QC) + 语音合成 (TTS)
*   **管理链接**：[小米开放平台控制台](https://platform.xiaomimimo.com/console/api-keys)
*   **获取 API Key**：登录后在「API 密钥管理」中创建。

## 3. Agnes (视频生成)
*   **用途**：AI 视频生成 (参考/备选)
*   **官网链接**：[Agnes AI](https://www.agnes-ai.com/)
*   **获取 API Key**：注册后获取。

## 4. 飞书 (Lark) - 可选
*   **用途**：SRT 时间轴提取 (飞书妙记)
*   **登录链接**：[飞书开放平台](https://open.feishu.cn/)

---

## 配置文件位置
请将获取的 API Key 填入 Skill 的配置文件中 (通常位于 `~/.agents/config/auto-video-skill-config.json`)。

```json
{
  "binghuo_api_key": "YOUR_BINGHUO_KEY",
  "xiaomi_api_key": "YOUR_XIAOMI_API_KEY",
  "agnes_api_key": "YOUR_AGNES_API_KEY"
}
```
