# coding=utf-8
from head import head, pp, pg
from base import getFullRule
from flask import Flask, request, abort, render_template
from requests import get
from urllib.parse import urlencode
from gevent import pywsgi


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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
            "url": "https://sub.xeton.dev/sub?target=clash&url="+url+"&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini",
            }
    url = "https://proxy-provider-converter.geniucker.top"\
          "/api/convert?" + urlencode(urltem)
    result = head\
        + pp.format(url, interval, url, interval, url, interval, url, interval, url, interval)\
        + pg + "rules:\n" + getFullRule()
    return result, {'Content-Type': 'text/yaml;charset=utf-8'}

@app.route("/test")
def test():
    url = request.args
    url = url.get("url")
    
    UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53"
    headers={'User_Agent':UA}
    return get(url, headers=headers).text


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=221, debug=False)
    server = pywsgi.WSGIServer(('0.0.0.0', 221), app)
    server.serve_forever()
