import requests
import json
import base64
import os
from io import BytesIO
from PIL import Image
import time

# 配置信息
API_KEY = "填写你的密钥"  # 替换为你的即梦API密钥
API_BASE = "https://api.aiyiapi.com"  # 替换为你的API地址
JIMENG_ENDPOINT = "/v1/images/generations"

# 请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def generate_image(prompt, size="1024x1024", model="jimeng-2.1", quality="standard", style="vivid", n=1):
    """
    使用即梦API生成图像
    
    参数:
    - prompt: 图像生成提示词
    - size: 图像尺寸 (1024x1024, 1195x512, 1024x576, 1024x682, 1024x768, 768x1024, 682x1024, 576x1024)
    - model: 模型名称 (jimeng-2.1（默认）, jimeng-2.0-pro, jimeng-2.0, jimeng-1.4, jimeng-xl-pro)
    - quality: 图像质量 (standard, hd)
    - style: 图像风格 (vivid, natural)
    
    返回:
    - 生成的图像URL列表和修改后的提示词
    """
    url = f"{API_BASE}{JIMENG_ENDPOINT}"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "n": n,
        "size": size,
        "quality": quality,
        "style": style
    }
    
    try:
        print(f"正在使用即梦API生成图像，提示词: '{prompt}'")
        print(f"请求URL: {url}")
        print(f"请求负载: {json.dumps(payload, ensure_ascii=False)}")
        
        response = requests.post(url, headers=headers, json=payload)
        
        print(f"响应状态码: {response.status_code}")
        print(f"响应头: {response.headers}")
        print(f"原始响应内容: {response.text[:500]}...")  # 打印前500个字符
        
        if response.status_code == 200:
            result = response.json()
            print("即梦图像生成成功!")
            
            # 提取图像URL和修改后的提示词
            image_urls = [item["url"] for item in result["data"]]
            revised_prompt = result["data"][0].get("revised_prompt", prompt)
            
            return {
                "success": True,
                "image_urls": image_urls,
                "revised_prompt": revised_prompt
            }
        else:
            print(f"即梦API错误: {response.status_code}")
            print(response.text)
            return {
                "success": False,
                "error": response.text
            }
    except Exception as e:
        print(f"即梦API请求异常: {e}")
        import traceback
        traceback.print_exc()  # 打印完整的异常堆栈
        return {
            "success": False,
            "error": str(e)
        }

def save_image(image_url, filename):
    """
    下载并保存即梦生成的图像
    
    参数:
    - image_url: 图像URL
    - filename: 保存的文件名
    """
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save(filename)
            print(f"即梦图像已保存为: {filename}")
            return True
        else:
            print(f"下载即梦图像失败: {response.status_code}")
            return False
    except Exception as e:
        print(f"保存即梦图像时出错: {e}")
        return False

def main():
    # 创建保存图像的目录
    output_dir = "jimeng_images"
    os.makedirs(output_dir, exist_ok=True)
    
    # 测试不同的提示词
    prompts = [
        "一只写实风格的猫坐在窗台上观看日落",
        "一座未来主义城市，有飞行汽车和霓虹灯",
        "一个水下场景，有色彩斑斓的珊瑚礁和热带鱼"
    ]
    
    for i, prompt in enumerate(prompts):
        # 使用即梦API生成图像
        result = generate_image(
            prompt=prompt,
            size="1024x1024",  # 可选: "1024x1024", "1195x512", "1024x576", "1024x682", "1024x768", "768x1024", "682x1024", "576x1024"
            model="jimeng-2.1",  # 可选: jimeng-2.1（默认）, jimeng-2.0-pro, jimeng-2.0, jimeng-1.4, jimeng-xl-pro
            quality="standard",  # 可选: "standard", "hd"
            style="vivid"  # 可选: "vivid", "natural"
        )
        
        if result["success"]:
            # 保存即梦生成的图像
            timestamp = int(time.time())
            for j, url in enumerate(result["image_urls"]):
                filename = f"{output_dir}/jimeng_{i+1}_{j+1}_{timestamp}.png"
                save_image(url, filename)
            
            # 打印修改后的提示词
            print(f"原始提示词: {prompt}")
            print(f"即梦修改后的提示词: {result['revised_prompt']}")
        else:
            print(f"即梦图像生成失败: {result.get('error', '未知错误')}")
        
        # 在请求之间添加延迟，避免API限制
        if i < len(prompts) - 1:
            print("等待3秒后继续下一个即梦API请求...")
            time.sleep(3)

if __name__ == "__main__":
    main() 