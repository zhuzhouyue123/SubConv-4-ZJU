"""
This module is to general a complete config for Clash
"""


from modules import snippet
from modules import head
import cache


def pack(url: list, interval, domain, zju, meta):
    regionDict, total = snippet.mkList(url)  # regions available and corresponding group name
    result = ""

    # create a snippet containing region groups
    regionGroups = ""
    for i in total.values():
        regionGroups += "      - " + i[1] + "\n"
    regionGroups = regionGroups[:-1]

    # head of config
    result += head.HEAD
    result += "\n"

    # proxies
    result += head.PROXIES_HEAD
    if zju["zjuPort"]:
        result += head.ZJU_PROXY.format(
            zju["zjuAddr"] if zju["zjuAddr"] else "localhost",
            zju["zjuPort"],
            ("\n    username: "+zju["zjuSocksUser"]) if zju["zjuSocksUser"] else "",
            ("\n    password: "+zju["zjuSocksPasswd"]) if zju["zjuSocksPasswd"] else ""
        )

    # proxy providers
    result += head.PROVIDER_HEAD
    for u in range(len(url)):
        result += head.PROVIDER_BASE0.format(u, url[u], interval, u)
        if meta is None:
            for i in regionDict[u]:
                result += head.PROVIDER_BASE1.format(i+str(u), url[u], interval, str(u), regionDict[u][i][0])
    result += "\n"

    result += head.PROXY_GROUP_HEAD
    # add proxy select
    result += head.PROXY_GROUP_PROXY_SELECT.format(regionGroups)
    # add manual select
    subscriptions = ""
    for u in range(len(url)):
        subscriptions += "      - subscription" + str(u) + "\n"
    subscriptions = subscriptions[:-1]
    result += head.PROXY_GROUP_PROXY_MANUAL_SELECT.format(subscriptions)
    # add auto select
    result += head.PROXY_GROUP_PROXY_AUTO_SELECT.format(subscriptions)
    # add fallback
    result += head.PROXY_GROUP_PROXY_FALLBACK.format(subscriptions)
    # add anycast
    result += head.PROXY_GROUP_PROXY_ANYCAST.format(subscriptions)
    # add zju groups
    for i in snippet.RULE_GROUP_LIST_ZJU:
        result += head.PROXY_GROUP_ZJU.format(
            i,
            "\n      - ZJU内网" if zju["zjuPort"] else "",
            regionGroups
        )
    # add proxy first groups
    for i in snippet.RULE_GROUP_LIST_PROXY_FIRST:
        result += head.PROXY_GROUP_PROXY_FIRST.format(i, regionGroups)
    # add direct forst groups
    for i in snippet.RULE_GROUP_LIST_DIRECT_FIRST:
        result += head.PROXY_GROUP_DIRECT_FIRST.format(i, regionGroups)
    # add reject first groups
    for i in snippet.RULE_GROUP_LIST_REJECT_FIRST:
        result += head.PROXY_GROUP_REJECT_FIRST.format(i)
    # add region groups
    if meta is None:
        for i in total:
            tmp = ""
            for u in range(len(url)):
                if i in regionDict[u]:
                    tmp += "      - " + i + str(u) + "\n"
            tmp = tmp[:-1]
            result += head.PROXY_GROUP_REGION_GROUPS.format(total[i][1], tmp)
        result += "\n"
    else:
        for i in total:
            result += head.PROXY_GROUP_REGION_GROUPS.format(total[i][1], subscriptions)
            result += "    filter: \"{}\"".format(total[i][0])
            result += "\n"
        result += "\n"

    # rules
    result += ("rules:\n  - DOMAIN,{},DIRECT\n".format(domain) + cache.cache)
    return result