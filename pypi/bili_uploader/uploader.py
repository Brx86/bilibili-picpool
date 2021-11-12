import requests

class BiliUploader:
    def __init__(self, cookies: dict, short_url=True) -> None:
        assert cookies['bili_jct']
        assert cookies['SESSDATA']

        self.cookies = cookies
        self.short_url = short_url

    def upload(self, bytes, filename=None):
        api_url = "https://api.vc.bilibili.com/api/v1/drawImage/upload"

        if filename is None:
            filename = str(hash(bytes))

        # 设置post参数
        files = {"file_up": (filename, bytes)}
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
            cookies=self.cookies,
            timeout=300,
        )

        # 解析返回值，得到图片链接
        img_url = r.json()["data"]["image_url"]

        if self.short_url:
            img_url = b23_link(img_url)

        return img_url

    def upload_file(self, filepath: str):
        with open(filepath, "rb") as f:
            img_file = f.read()
        return self.upload(img_file, filename=filepath.split("/")[-1])


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
