"""
This module is to general a complete config for Clash
"""


from modules import snippet
from modules import head
import config
import cache


def pack(url: list, urlstandby, content: str, interval, domain, short):
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


    # proxy providers
    result += head.PROVIDER_HEAD
    for u in range(len(url)):
        result += head.PROVIDER_BASE0.format(u, url[u], interval, u)
    if urlstandby:
        for u in range(len(urlstandby)):
            result += head.PROVIDER_BASE0.format("sub"+str(u), urlstandby[u], interval, "sub"+str(u))
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
    standby = subscriptions
    if urlstandby:
        for u in range(len(urlstandby)):
            standby += "      - subscriptionsub" + str(u) + "\n"
    standby = standby[:-1]
    subscriptions = subscriptions[:-1]
    result += head.PROXY_GROUP_PROXY_MANUAL_SELECT.format(standby)
    # add auto select
    result += head.PROXY_GROUP_PROXY_AUTO_SELECT.format(subscriptions)
    # add fallback
    result += head.PROXY_GROUP_PROXY_FALLBACK.format(subscriptions)

    # add proxy groups
    for group in config.custom_proxy_group:
        type = group["type"]
        if type == "load-balance":
            region = group.get("region")
            if region is None:
                result += head.PROXY_GROUP_PROXY_ANYCAST.format(group["name"], subscriptions)
            else:
                tmp = []
                for i in region:
                    if i in total:
                        tmp.append(total[i][0])
                if len(tmp) > 0:
                    result += head.PROXY_GROUP_PROXY_ANYCAST.format(group["name"], subscriptions)
                    result += "    filter: \"{}\"".format("|".join(tmp))
                    result += "\n"

        elif type == "select":
            prior = group["prior"]
            if prior == "DIRECT":
                result += head.PROXY_GROUP_DIRECT_FIRST.format(group["name"], regionGroups)
            elif prior == "REJECT":
                result += head.PROXY_GROUP_REJECT_FIRST.format(group["name"], regionGroups)
            else:
                result += head.PROXY_GROUP_PROXY_FIRST.format(group["name"], regionGroups)

    # add region groups
    for i in total:
        result += head.PROXY_GROUP_REGION_GROUPS.format(total[i][1], subscriptions)
        result += "    filter: \"{}\"".format(total[i][0])
        result += "\n"
    result += "\n"

    # rules
    result += ("rules:\n  - DOMAIN,{},DIRECT\n".format(domain) + cache.cache)
    return result