# coding=utf-8
from modules import pack
from modules import snippet
import re
from flask import Flask, request, render_template 
import requests
from urllib.parse import urlencode, unquote
from gevent import pywsgi


app = Flask(__name__)


# subscription converter api
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

    content = []  # the proxies of original subscriptions
    for i in range(len(url)):
        # the test of response
        respText = requests.get(url[i], headers={'User-Agent':'clash'}).text
        content.append(snippet.parseYAML(respText))
        url[i] = "{}provider?{}".format(request.url_root, urlencode({"url": url[i]}))

    # get the domain or ip of this api to add rule for this
    domain = re.search(r"([^:]+)(:\d{1,5})?", request.host).group(1)
    # generate the subscription
    result = pack.pack(url=url, content=content, interval=interval, domain=domain, zju=zju, meta=meta)
    return result, headers


# provider converter
@app.route("/provider")
def provider():
    headers = {'Content-Type': 'text/yaml;charset=utf-8'}
    url = request.args.get("url")
    return snippet.parseYAML(
        requests.get(url, headers={'User-Agent':'clash'}).text
    ), headers


if __name__ == "__main__":
    # Debug
    # app.run(host="0.0.0.0", port=443, debug=True)
    # Production
    server = pywsgi.WSGIServer(('0.0.0.0', 443), app)
    server.serve_forever()
