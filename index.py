# coding=utf-8
from modules import pack
from modules import indexhtml
import os
from flask import Flask, request, abort
import requests
from urllib.parse import urlencode
from gevent import pywsgi


app = Flask(__name__)


# mainpage as well as simple description
@app.route("/")
def index():
    return indexhtml.content.format(*((request.url_root,)*3)), {'Content-Type': 'text/html;charset=utf-8'}


# api
@app.route("/sub")
def sub():
    url = request.args
    # get interval
    if "interval" in url:
        interval = url["interval"]
    else:
        interval = "600"
    # get the url of original subscription
    url = url.get("url")

    headers = {'Content-Type': 'text/yaml;charset=utf-8'}
    originalHeaders = requests.head(url, headers={'User-Agent':'clash'}).headers
    if 'subscription-userinfo' in originalHeaders:
        headers['subscription-userinfo'] = originalHeaders['subscription-userinfo']
    if 'Content-Disposition' in originalHeaders:
        headers['Content-Disposition'] = originalHeaders['Content-Disposition'].replace("attachment", "inline")

    urltem = {
        "target": "clash",
        "url": url,
    }
    url = os.environ.get("provider_converter")\
        + "/api/convert?" + urlencode(urltem)
    result = pack.pack(url, interval)
    return result, headers


if __name__ == "__main__":
    # Debug
    # app.run(host="0.0.0.0", port=221, debug=True)
    # Production
    server = pywsgi.WSGIServer(('0.0.0.0', 443), app)
    server.serve_forever()
