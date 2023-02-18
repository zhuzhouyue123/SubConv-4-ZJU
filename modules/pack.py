"""
This module is to general a complete config for Clash
"""


from modules import snippet
from modules import head
import cache


def pack(url, interval, domain, zju):
    regionDict = snippet.mkList(url)  # regions available and corresponding group name
    result = ""

    # create a snippet containing region groups
    regionGroups = ""
    for i in regionDict.values():
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
    result += head.PROVIDER_HEAD.format(url, interval)
    for i in regionDict:
        result += head.PROVIDER_BASE.format(i, url, interval, regionDict[i][0])
    result += "\n"

    result += head.PROXY_GROUP_HEAD
    # add proxy select
    result += head.PROXY_GROUP_PROXY_SELECT.format(regionGroups)
    # add manual select
    result += head.PROXY_GROUP_PROXY_MANUAL_SELECT
    # add auto select
    result += head.PROXY_GROUP_PROXY_AUTO_SELECT
    # add common auto select
    result += head.PROXY_GROUP_PROXY_COMMON_AUTO_SELECT.fomat(regionGroups)
    # add fallback
    result += head.PROXY_GROUP_PROXY_FALLBACK
    # add anycast
    result += head.PROXY_GROUP_PROXY_ANYCAST
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
    for i in regionDict:
        result += head.PROXY_GROUP_REGION_GROUPS.format(regionDict[i][1], i)
    result += "\n"

    # rules
    result += ("rules:\n  - DOMAIN,{},DIRECT\n".format(domain) + cache.cache)
    return result