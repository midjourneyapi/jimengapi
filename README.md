# 即梦 API 图像生成演示

这个项目是一个简单的即梦 AI 图像生成 API 的演示程序。即梦是一个强大的 AI 图像生成服务，通过简单的文本提示词就能创建高质量的图像。本项目通过 aiyiapi 平台聚合全球 AI API，实现一个代码轻松接入即梦服务的功能。此接口完全兼容 OpenAI DALL·E 3 的接口规范，可直接替换使用，方便开发者无缝切换或集成。

## 功能特点

- 通过文本提示词生成 AI 图像
- 支持多种图像尺寸 (1024x1024, 1195x512, 1024x576, 1024x682, 1024x768, 768x1024, 682x1024, 576x1024)
- 支持多种即梦模型 (jimeng-2.1, jimeng-2.0-pro, jimeng-2.0, jimeng-1.4, jimeng-xl-pro)
- 可调整图像质量和风格
- 自动保存生成的图像到本地文件夹
- 详细的日志输出，便于调试和了解 API 响应

## 使用方法

1. 克隆此仓库到本地
2. 安装所需依赖：`pip install requests pillow`
3. 在 `jimeng.py` 文件中填入您的 aiyiapi 平台 API 密钥
4. 运行脚本：`python jimeng.py`

## 代码示例

### 配置选项

- **API_KEY**: 您的 aiyiapi 平台 API 密钥（用于访问聚合的全球 AI API 服务，包括即梦 API）
- **API_BASE**: API 基础 URL，默认为 `"https://aiyiapi.com"`（aiyiapi 平台提供统一的接口分发）
- **提示词**: 描述您想要生成的图像内容
- **尺寸**: 支持多种图像尺寸比例
- **模型**: 选择不同的即梦模型版本
- **质量**: 标准或高清
- **风格**: 生动或自然

## 注意事项

- 请确保您有有效的 aiyiapi 平台 API 密钥（注册于 [aiyiapi.com](https://aiyiapi.com/)）
- API 可能有请求频率限制，脚本中已添加请求间隔
- 生成的图像将保存在 `jimeng_images` 文件夹中
- aiyiapi 平台是聚合全球 AI API 的服务，通过它您可以轻松调用即梦及其他主流 AI 模型
- 此接口完全兼容 OpenAI DALL·E 3 的接口规范，原有 DALL·E 3 代码可直接使用，只需更换 API 密钥和基础 URL 即可

## 即梦 API 参数说明

即梦 API 支持以下参数：  
*(此处可根据实际 API 文档补充具体参数说明)*

## 示例图像

运行脚本后，您将在 `jimeng_images` 文件夹中找到生成的图像。每个图像都会以时间戳命名，以避免文件覆盖。

## 许可证

MIT License

---

欢迎贡献代码或提出建议，希望这个演示项目能帮助您快速上手即梦 API 的使用，同时体验 aiyiapi 平台聚合全球 AI API 的便利！
