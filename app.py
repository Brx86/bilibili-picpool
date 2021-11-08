import os
from flask import Flask, app, request
from uploader import image_upload, b23_link

app = Flask(__name__)
base_path = f"{os.path.abspath(os.path.dirname(__file__))}/static/"  # 定义一个根目录 用于保存图片用


@app.route("/", methods=["POST"])
def upload():
    img = request.files.get("file")
    img_name = img.filename
    file_path = base_path + img_name
    img.save(file_path)
    url = image_upload(file_path, 0)
    return url


@app.route("/long", methods=["POST"])
def upload_long():
    img = request.files.get("file")
    img_name = img.filename
    file_path = base_path + img_name
    img.save(file_path)
    url = image_upload(file_path, 1)
    return url


@app.route("/short", methods=["POST"])
def upload_short():
    img = request.files.get("file")
    img_name = img.filename
    file_path = base_path + img_name
    img.save(file_path)
    url = image_upload(file_path, 2)
    return url


if __name__ == "__main__":
    n = 0
    app.run(host="0.0.0.0", port=2000, debug=1, threaded=0)
