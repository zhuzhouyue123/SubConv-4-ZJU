
ruleset = [
    ["✔ ZJU", "https://raw.githubusercontent.com/wolf2003rain/sub-conv-4-ZJU-deploy/custom-rules/tmp.list"],
    ["🎯 全球直连", "https://raw.githubusercontent.com/wolf2003rain/sub-conv-4-ZJU-deploy/custom-rules/direct.list"],
    ["🛸 PT站", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/PrivateTracker.list"],
    ["✔ ZJU", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/ZJU.list"],
    ["📃 ZJU More Scholar", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/ZJU-More-Scholar.list"],
    ["🤖 ChatBot", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/ChatBot.list"],
    ["🎯 全球直连", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/LocalAreaNetwork.list"],
    ["🎯 全球直连", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/UnBan.list"],
    ["🛑 广告拦截", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/BanAD.list"],
    ["🍃 应用净化", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/BanProgramAD.list"],
    ["🛑 广告拦截", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/BanEasyList.list"],
    ["🛑 广告拦截", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/BanEasyListChina.list"],
    ["🛡️ 隐私防护", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/BanEasyPrivacy.list"],
    ["📢 谷歌FCM", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/GoogleFCM.list"],
    # ["🎯 全球直连", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/GoogleCN.list"],
    ["🎯 全球直连", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Adobe.list"],
    ["Ⓜ️ 微软云盘", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/OneDrive.list"],
    ["Ⓜ️ 微软服务", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Microsoft.list"],
    ["🍎 苹果服务", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Apple.list"],
    ["📲 电报消息", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Telegram.list"],
    ["🎶 网易音乐", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/NetEaseMusic.list"],
    ["🎶 Spotify", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Spotify.list"],
    ["🎮 游戏平台", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Epic.list"],
    ["🎮 游戏平台", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Origin.list"],
    ["🎮 游戏平台", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Sony.list"],
    ["🎮 游戏平台", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Steam.list"],
    ["🎮 游戏平台", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Nintendo.list"],
    ["📹 油管视频", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/YouTube.list"],
    ["🎥 奈飞视频", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Netflix.list"],
    ["📺 巴哈姆特", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Bahamut.list"],
    ["📺 哔哩哔哩", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/BilibiliHMT.list"],
    ["📺 哔哩哔哩", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Ruleset/Bilibili.list"],
    ["🌏 国内媒体", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/ChinaMedia.list"],
    ["🌍 国外媒体", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/ProxyMedia.list"],
    ["🚀 节点选择", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/ProxyGFWlist.list"],
    ["🎯 全球直连", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/ChinaIp.list"],
    ["🎯 全球直连", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/ChinaDomain.list"],
    ["🎯 全球直连", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/ChinaCompanyIp.list"],
    ["🎯 全球直连", "https://raw.githubusercontent.com/ZJU-Rule/ZJU-Rule/master/Clash/Download.list"],
    ["🎯 全球直连", "[]GEOIP,CN"],
    ["🐟 漏网之鱼", "[]FINAL"]
]

custom_proxy_group = [
    {
        "name": "🔮 负载均衡",
        "type": "load-balance",
    },
    {
        "name": "🔮 香港负载均衡",
        "type": "load-balance",
        "region": ["HK"]
    },
    {
        "name": "✔ ZJU",
        "type": "select",
        "ZJU": True,
    },
    {
        "name": "📃 ZJU More Scholar",
        "type": "select",
        "ZJU": True,
    },
    {
        "name": "🤖 ChatBot",
        "type": "select",
        "prior": "PROXY"
    },
    {
        "name": "📲 电报消息",
        "type": "select",
        "prior": "PROXY"
    },
    {
        "name": "📹 油管视频",
        "type": "select",
        "prior": "PROXY"
    },
    {
        "name": "🎥 奈飞视频",
        "type": "select",
        "prior": "PROXY"
    },
    {
        "name": "📺 巴哈姆特",
        "type": "select",
        "prior": "PROXY"
    },
    {
        "name": "📺 哔哩哔哩",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🌍 国外媒体",
        "type": "select",
        "prior": "PROXY"
    },
    {
        "name": "🌏 国内媒体",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "📢 谷歌FCM",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "Ⓜ️ 微软云盘",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "Ⓜ️ 微软服务",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🍎 苹果服务",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🎮 游戏平台",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🎶 网易音乐",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🎶 Spotify",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🛸 PT站",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🎯 全球直连",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🛑 广告拦截",
        "type": "select",
        "prior": "REJECT"
    },
    {
        "name": "🍃 应用净化",
        "type": "select",
        "prior": "REJECT"
    },
    {
        "name": "🛡️ 隐私防护",
        "type": "select",
        "prior": "REJECT"
    },
    {
        "name": "🐟 漏网之鱼",
        "type": "select",
        "prior": "PROXY"
    }
]
