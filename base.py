from ruleList import ruleList
from re import search
from requests import get


def getRule(sort, url):
    result = ""
    item = get(url).text
    item = item.split("\n")
    i = 0
    while(i < len(item)):
        tem = item[i]
        if "" == tem or "#" == tem[0]\
                or "USER-AGENT" in tem\
                or "URL-REGEX" in tem:
            item.remove(tem)
            i -= 1
        else:
            tem2 = search("(.+,.+)(,.+)", tem)
            if tem2 is not None:
                item[i] = tem2.group(1) + "," + sort + tem2.group(2)
            else:
                item[i] += "," + sort
        i += 1
    for i in range(len(item)):
        result += " - " + item[i] + "\n"
    return result


def getFullRule():
    for i in ruleList:
        result += getRule(i[0], i[1])
    result += """ - GEOIP,CN,🎯 全球直连
 - MATCH,🐟 漏网之鱼"""
    return result


