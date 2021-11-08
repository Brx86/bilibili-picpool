# bilibili-picpool

## 简介: 

- 白嫖B站图片外链，可以用作图床，也可以用于在B站评论区发图


## 注意事项:

- 合理使用, 请勿滥用, 如有后果概不负责

#### 环境需求:

python >= 3.6

#### 第三方库:

flask, requests

#### 使用方法:

网页登陆Bilibili帐号，查看Cookie，将bili_jct和SESSDATA的值填入config.py

**使用例:**

1. 在当前文件夹执行`python uploader.py <图片路径>`

```bash
❯ py uploader.py test.png
图片上传中...
图片链接: http://i0.hdslb.com/bfs/album/cefaa6a1e3a5f8674f36192dc5f9251dca620540.png
短网址:   https://b23.tv/CqfmCz
```



2. 在当前文件夹执行`python app.py`运行flask接口，然后使用post上传图片，获得图片地址

```bash
# shell命令

❯ curl -F "file=@test.png" http://127.0.0.1:2000/short
https://b23.tv/pb3KZo

❯ curl -F "file=@test.png" http://127.0.0.1:2000/long
http://i0.hdslb.com/bfs/album/cefaa6a1e3a5f8674f36192dc5f9251dca620540.png

❯ curl -F "file=@test.png" http://127.0.0.1:2000     
{
  "img_url": "http://i0.hdslb.com/bfs/album/cefaa6a1e3a5f8674f36192dc5f9251dca620540.png", 
  "short_url": "https://b23.tv/AKwXcE"
}
```

```python
# python脚本

import requests

response = requests.post(
    "http://127.0.0.1:2000", files={"file": open("test.png", "rb")}
)

print(response.text)

# 运行结果
{
  "img_url": "http://i0.hdslb.com/bfs/album/cefaa6a1e3a5f8674f36192dc5f9251dca620540.png", 
  "short_url": "https://b23.tv/AKwXcE"
}

```

