"""
This module is to general a complete config for Clash
"""


import snippet
import rule
import head


def pack(url, interval):
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
    # add fallback
    result += head.PROXY_GROUP_PROXY_FALLBACK
    # add anycast
    result += head.PROXY_GROUP_PROXY_ANYCAST
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
    result += ("rules:\n" + rule.getFullRule())
    return result