# coding=utf-8
import snippet
import indexhtml
import os
from flask import Flask, request, abort
from requests import get
from urllib.parse import urlencode
from gevent import pywsgi


app = Flask(__name__)


@app.route("/")
def index():
    return indexhtml.content.format(*((request.url_root,)*3)), {'Content-Type': 'text/html;charset=utf-8'}


@app.route("/sub")
def sub():
    # return "Hello World!"
    url = request.args
    if "interval" in url:
        interval = url["interval"]
    else:
        interval = "600"
    url = url.get("url")
    status_code = get(url).status_code
    if 200 != status_code:
        pass
        # abort(status_code)
        # return
    urltem = {
            "target": "clash",
            "url": url,
            }
    url = os.environ.get("provider_converter")\
        + "/api/convert?" + urlencode(urltem)
    result = snippet.pack(url, interval)
    return result, {'Content-Type': 'text/yaml;charset=utf-8'}


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=221, debug=True)
    server = pywsgi.WSGIServer(('0.0.0.0', 443), app)
    server.serve_forever()
