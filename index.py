# coding=utf-8
from head import head, pp1, pp2, pp3, pg
from base import getFullRule
from flask import Flask, request, abort, render_template
from requests import get
from urllib.parse import urlencode


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
        abort(status_code)
        return
    urltem = {
            "target": "clash",
            "url": url,
            }
    url = "https://proxy-provider-converter.geniucker.vercel.app"\
          "/api/convert?" + urlencode(urltem)
    result = head + pp1 + url + pp2 + interval + pp3 + pg\
                  + "rules:\n" + getFullRule()
    return result, {'Content-Type': 'text/yaml;charset=utf-8'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=221, debug=False)
