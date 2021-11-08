import os, requests
from config import cookies

# 定义上传函数
def image_upload(file_path, arg):
    # api地址
    api_url = "https://api.vc.bilibili.com/api/v1/drawImage/upload"

    # 打开图片文件
    with open(file_path, "rb") as f:
        img_file = f.read()

    # 设置post参数
    files = {"file_up": (file_path, img_file)}
    data = {
        "biz": "draw",
        "category": "daily",
    }
    headers = {
        "Origin": "https://t.bilibili.com",
        "Referer": "https://t.bilibili.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    }

    # 向api发送post请求
    r = requests.post(
        api_url,
        files=files,
        data=data,
        headers=headers,
        cookies=cookies,
        timeout=300,
    )

    # 解析返回值，得到图片链接
    img_url = r.json()["data"]["image_url"]
    if arg == 0:
        short_url = b23_link(img_url)
        # 输出结果
        print(f"图片链接: {img_url}\n短网址:   {short_url}")
        return {"img_url": img_url, "short_url": short_url}
    elif arg == 1:
        return img_url
    elif arg == 2:
        short_url = b23_link(img_url)
        return short_url


# 定义b23短链函数
def b23_link(url):
    # api地址
    api_url = "https://api.bilibili.com/x/share/click"

    # 设置post参数
    data = {
        "build": 10000,
        "buvid": "archlinux",
        "platform": "archlinux",
        "share_channel": "COPY",
        "share_id": "public.webview.0.0.pv",
        "share_mode": 1,
        "oid": url,
    }

    # 请求api得到短链接
    r = requests.post(api_url, data=data)
    return r.json()["data"]["content"]


if __name__ == "__main__":
    if len(os.sys.argv) == 2:
        file_name = os.sys.argv[1]
        file_path = os.path.abspath(file_name)
        print("图片上传中...")
    else:
        print("格式有误！上传示例图片example.png...")
        file_path = os.path.join(os.sys.path[0], "example.png")
    image_upload(file_path, 0)
