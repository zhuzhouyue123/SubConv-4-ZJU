"""
This module is to get the list of regions available in orginal subscription
"""


import re


# regions and the regular expression to match them
REGION_DICT = {
        "HK": [r"HK|Hong|Kong|HGC|WTT|CMI|港", "🇭🇰 香港节点"],
        "TW": [r"TW|Taiwan|新北|彰化|CHT|台|HINET", "🇨🇳 台湾节点"],
        "SG": [r"SG|Singapore|狮城|^新[^节北]|[^刷更]新[^节北]", "🇸🇬 狮城节点"],
        "JP": [r"JP|Japan|Tokyo|Osaka|Saitama|东京|大阪|埼玉|日", "🇯🇵 日本节点"],
        "KR": [r"KO?R|Korea|首尔|韩|韓", "🇰🇷 韩国节点"],
        "US": [r"US|America|United.*?States|美|波特兰|达拉斯|俄勒冈|凤凰城|费利蒙|硅谷|拉斯维加斯|洛杉矶|圣何塞|圣克拉拉|西雅图|芝加哥", "🇺🇸 美国节点"]
        }

# parse yaml
def parseYAML(content):
    import yaml
    return yaml.safe_dump(
        {"proxies": yaml.load(content, Loader=yaml.FullLoader).get("proxies")},
        allow_unicode=True,  # display characters like Chinese
        sort_keys=False  # keep the original sequence
    )

# create a dict containg resions and corresponding proxy group
def mkList(content: list):
    result = []
    total = {}
    for u in content:
        tmp = {}
        # preprocess the content
        contentTmp = re.findall(r"- name: (.+)", u)
        contentTmp = ",".join(contentTmp)
        for i in REGION_DICT:
            if re.search(REGION_DICT[i][0], contentTmp, re.I) is not None:
                tmp[i] = REGION_DICT[i]
                total[i] = REGION_DICT[i]
        result.append(tmp)
    return result, total