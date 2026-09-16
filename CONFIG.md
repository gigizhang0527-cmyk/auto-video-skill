
# 🔑 API 配置指南

本 Skill 依赖以下 API 服务。请在使用前完成配置。

## 1. 炳火 API (BingHuo)
*   **用途**：生图 (gpt-image-2) + 动画 (Seedance/SD2.5)
*   **注册链接**：[点击注册 (使用推荐码)](https://api.7tai.cc/register?code=YOUR_CODE_HERE)
*   **获取 API Key**：登录后在「个人中心」获取 API Key。
*   **价格参考**：请参考 [官方价格表](https://api.7tai.cc/pricing)。

## 2. 小米 MiMo (视觉审片)
*   **用途**：视频画面质量检查 (QC)
*   **登录链接**：[小米账号统一登录](https://account.xiaomi.com/pass/qr/login)
*   **获取 Token**：登录后在开发者中心申请 MiMo-v2.5 模型权限。

## 3. MiniMax (TTS)
*   **用途**：语音克隆与合成
*   **登录链接**：[MiniMax 开放平台](https://www.minimaxi.com/)
*   **获取 API Key**：在「API 密钥管理」中创建。

## 4. 飞书 (Lark) - 可选
*   **用途**：SRT 时间轴提取 (飞书妙记)
*   **登录链接**：[飞书开放平台](https://open.feishu.cn/)

---

## 配置文件位置
请将获取的 API Key 填入 Skill 的配置文件中 (通常位于 `~/.agents/config/kepu-video-config.json`)。

```json
{
  "binghuo_api_key": "YOUR_BINGHUO_KEY",
  "mimo_api_key": "YOUR_MIMO_KEY",
  "minimax_api_key": "YOUR_MINIMAX_KEY"
}
```
