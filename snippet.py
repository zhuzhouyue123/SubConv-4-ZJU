import requests
import re
import head
import rule


RULE_GROUP_LIST_PROXY_FIRST = [
        "📲 电报消息",
        "📹 油管视频",
        "🎥 奈飞视频",
        "📺 巴哈姆特",
        "🎥 奈飞节点",
        "🌍 国外媒体",
        "🐟 漏网之鱼",
        ]
RULE_GROUP_LIST_DIRECT_FIRST = [
        "📺 哔哩哔哩",
        "🌏 国内媒体",
        "📢 谷歌FCM",
        "Ⓜ️ 微软云盘",
        "Ⓜ️ 微软服务",
        "🍎 苹果服务",
        "🎮 游戏平台",
        "🎶 网易音乐",
        "🎯 全球直连",
        ]
RULE_GROUP_LIST_REJECT_FIRST = [
        "🛑 广告拦截",
        "🍃 应用净化",
        ]
REGION_DICT = {
        "HK": [r"HK|Hong|Kong|HGC|WTT|CMI|港", "🇭🇰 香港节点"],
        "TW": [r"TW|Taiwan|新北|彰化|CHT|台|HINET", "🇨🇳 台湾节点"],
        "SG": [r"SG|Singapore|新加坡|狮城|新", "🇸🇬 狮城节点"],
        "JP": [r"JP|Japan|Tokyo|Osaka|Saitama|日本|东京|大阪|埼玉|日", "🇯🇵 日本节点"],
        "KR": [r"KO?R|Korea|首尔|韩|韓", "🇰🇷 韩国节点"],
        "US": [r"US|America|United.*?States|美|波特兰|达拉斯|俄勒冈|凤凰城|费利蒙|硅谷|拉斯维加斯|洛杉矶|圣何塞|圣克拉拉|西雅图|芝加哥", "🇺🇸 美国节点"]
        }


def mkList(url):
    result = {}
    content = requests.get(url).text
    for i in REGION_DICT:
        if re.search(REGION_DICT[i][0], content, re.I) is not None:
            result[i] = REGION_DICT[i]
    return result


def pack(url, interval):
    regionDict = mkList(url)
    result = ""
    regionGroups = ""
    for i in regionDict.values():
        regionGroups += "      - " + i[1] + "\n"
    regionGroups = regionGroups[:-1]

    result += head.HEAD

    # proxy providers
    result += head.PROVIDER_HEAD.format(url, interval)
    for i in regionDict:
        result += head.PROVIDER_BASE.format(i, url, interval, regionDict[i][0])

    result += head.PROXY_GROUP_HEAD
    # proxy select
    result += head.PROXY_GROUP_PROXY_SELECT.format(regionGroups)
    # manual select
    result += head.PROXY_GROUP_PROXY_MANUAL_SELECT
    # auto select
    result += head.PROXY_GROUP_PROXY_AUTO_SELECT
    # fallback
    result += head.PROXY_GROUP_PROXY_FALLBACK
    # anycast
    result += head.PROXY_GROUP_PROXY_ANYCAST
    # proxy first groups
    for i in RULE_GROUP_LIST_PROXY_FIRST:
        result += head.PROXY_GROUP_PROXY_FIRST.format(i, regionGroups)
    # direct forst groups
    for i in RULE_GROUP_LIST_DIRECT_FIRST:
        result += head.PROXY_GROUP_DIRECT_FIRST.format(i, regionGroups)
    # reject first groups
    for i in RULE_GROUP_LIST_REJECT_FIRST:
        result += head.PROXY_GROUP_REJECT_FIRST.format(i)
    # region groups
    for i in regionDict:
        result += head.PROXY_GROUP_REGION_GROUPS.format(regionDict[i][1], i)

    # ruls
    result += ("rules:\n" + rule.getFullRule())
    return result
