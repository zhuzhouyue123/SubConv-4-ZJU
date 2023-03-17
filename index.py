# coding=utf-8
from modules import pack
import os
import re
from flask import Flask, request, render_template 
import requests
from urllib.parse import urlencode, unquote
from gevent import pywsgi


app = Flask(__name__)


# mainpage as well as simple description
@app.route("/")
def index():
    return render_template("index.html")


# api
@app.route("/sub")
def sub():
    args = request.args
    # get interval
    if "interval" in args:
        interval = args["interval"]
    else:
        interval = "600"
    # get port of zju connect 
    zju = {
        "zjuPort": args.get("zjuport"),
        "zjuSocksUser": args.get("zjusocksuser"),
        "zjuSocksPasswd": args.get("zjusockspasswd"),
        "zjuAddr": args.get("zjuaddr")
    }

    meta = args.get("meta")  # judge if using the config of clash meta

    # get the url of original subscription
    url = args.get("url")
    url = re.split(r"[|\n]", url)
    # remove empty lines
    url = list(filter(lambda x: x!="", url)) 

    # get original headers
    headers = {'Content-Type': 'text/yaml;charset=utf-8'}
    # if there's only one subscription, return userinfo
    if len(url) == 1:
        originalHeaders = requests.head(url[0], headers={'User-Agent':'clash'}).headers
        if 'subscription-userinfo' in originalHeaders:  # containing info about ramaining flow
            headers['subscription-userinfo'] = originalHeaders['subscription-userinfo']
        if 'Content-Disposition' in originalHeaders:  # containing filename
            headers['Content-Disposition'] = originalHeaders['Content-Disposition'].replace("attachment", "inline")

    urltem = []
    for i in url:
        urltem.append({"target": "clash", "url": i}
    )
    providerConvUrl = os.environ.get("provider_converter")
    domain = re.match(r"https?://(.+)", providerConvUrl).group(1)
    urlAfterConv = []
    for i in urltem:
        urlAfterConv.append(providerConvUrl + "/api/convert?" + urlencode(i))
    result = pack.pack(url=urlAfterConv, interval=interval, domain=domain, zju=zju, meta=meta)
    return result, headers


if __name__ == "__main__":
    # Debug
    app.run(host="0.0.0.0", port=443, debug=True)
    # Production
    # server = pywsgi.WSGIServer(('0.0.0.0', 443), app)
    # server.serve_forever()
