# coding=utf-8
from ruleList import ruleList
from base import head, pp1, pp2, pg
from flask import Flask, request
from requests import get
app = Flask(__name__)


def getRule(sort, url):
    result = ""
    item = get(url).text
    item = item.split("\n")
    i = 0
    while(i < len(item)):
        tem = item[i]
        if "" == tem or "#" == tem[0]:
            item.remove(tem)
            i -= 1
        i += 1
    for i in range(len(item)):
        result += " - " + item[i] + "," + sort + "\n"
    return result


def getFullRule():
    result = ""
    for i in ruleList:
        result += getRule(i[0], i[1])
    return result


@app.route("/sub")
def welcome():
    # return "Hello World!"
    url = request.args.get("url")
    status_code = get(url).status_code
    if 200 != status_code:
        abort(status_code)
        return
    url = "https://proxy-provider-converter.geniucker.vercel.app"\
          "/api/convert?target=clash&url=" + url
    result = head + pp1 + url + pp2 + pg + "rules:\n" + getFullRule()
    return result, {'Content-Type': 'text/yaml;charset=utf-8'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=221, debug=False)
