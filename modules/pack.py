"""
This module is to general a complete config for Clash
"""


from modules import snippet
from modules import head
import config
import cache


def pack(url: list, content: str, interval, domain, zju, meta, short):
    regionDict, total = snippet.mkList(content)  # regions available and corresponding group name
    result = ""

    # create a snippet containing region groups
    regionGroups = ""
    for i in total.values():
        regionGroups += "      - " + i[1] + "\n"
    regionGroups = regionGroups[:-1]

    if short is None:
        # head of config
        result += head.HEAD
        result += "\n"

        # dns
        result += head.DNS
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
    tmp = "\n"
    for group in config.custom_proxy_group:
        if group["type"] == "load-balance":
            tmp += "      - " + group["name"] + "\n"
    tmp += regionGroups
    result += head.PROXY_GROUP_PROXY_SELECT.format(tmp)
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

    # add proxy groups
    for group in config.custom_proxy_group:
        type = group["type"]
        if type == "load-balance":
            location = group.get("location")
            if location is None:
                result += head.PROXY_GROUP_PROXY_ANYCAST.format(group["name"], subscriptions)
            else:
                if meta is None:
                    tmp = ""
                    for i in location:
                        if i in total:
                            for u in range(len(url)):
                                if i in regionDict[u]:
                                    tmp += "      - " + i + str(u) + "\n"
                    if tmp != "":
                        result += head.PROXY_GROUP_PROXY_ANYCAST.format(group["name"], tmp)
                else:
                    tmp = []
                    for i in location:
                        if i in total:
                            tmp.append(total[i][0])
                    if len(tmp) > 0:
                        result += head.PROXY_GROUP_PROXY_ANYCAST.format(group["name"], subscriptions)
                        result += "    filter: \"{}\"".format("|".join(tmp))
                        result += "\n"

        elif type == "select":
            if group.get("ZJU"):
                    result += head.PROXY_GROUP_ZJU.format(
                        group["name"],
                        "\n      - ZJU内网" if zju["zjuPort"] else "",
                        regionGroups
                    )
            else:
                prior = group["prior"]
                if prior == "DIRECT":
                    result += head.PROXY_GROUP_DIRECT_FIRST.format(group["name"], regionGroups)
                elif prior == "REJECT":
                    result += head.PROXY_GROUP_REJECT_FIRST.format(group["name"], regionGroups)
                else:
                    result += head.PROXY_GROUP_PROXY_FIRST.format(group["name"], regionGroups)

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