from bili_uploader import BiliUploader

cookies = {
    "bili_jct": "",
    "SESSDATA": "",
}

b_uploader = BiliUploader(cookies=cookies, short_url=True)

with open("test.png", 'rb') as f:
    data = f.read()

print("Upload bytes:")
print(b_uploader.upload(data))

print("Upload file:")
print(b_uploader.upload_file("test.png"))