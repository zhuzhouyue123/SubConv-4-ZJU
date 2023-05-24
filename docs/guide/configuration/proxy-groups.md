# Proxy Groups
There are some fixed groups containing `🚀 节点选择`, `🚀 手动切换`, `♻️ 自动选择`, `🔯 故障转移` and regional groups such as `🇭🇰 香港节点`. Other groups can be customized by config file `config.py`. You can also customized rule groups. For example, you can   
As You see, the config is in Python syntax.  I will express the usage next.  

## Customize proxy-groups
a valid will be like this:  
```Python
custom_proxy_group = [
    {
        "name": "🔮 负载均衡",
        "type": "load-balance",
    },
    {
        "name": "🔮 香港负载均衡",
        "type": "load-balance",
        "location": ["HK"]
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
        "name": "🎶 网易音乐",
        "type": "select",
        "prior": "DIRECT"
    },
    {
        "name": "🛑 广告拦截",
        "type": "select",
        "prior": "REJECT"
    },
    {
        "name": "🐟 漏网之鱼",
        "type": "select",
        "prior": "PROXY"
    }
]
```
2 types of groups are supported: `load-balance` and `select`  
As for `load-balance` group, there are 3 fields:
- `"name"`: the name of the group, the datatype should be `str`  
- `"type"`: should be `"load-balance"`, the datatype is `str`  
- `"region"`: regions you want to add to one load-balance group. If not specified, all proxies will appear. The datatype of this field should be `list`, the type of each element in the `list` should be `str`. The possible values are `"HK"`, `"TW"`, `"KR"`, `"JP"`, `"US"`, `"SG"`  

As for `select` group, there are 4 fields:  
- `"name"`: the name of the group, the datatype should be `str`  
- `"type"`: should be `"select"`, the datatype is `str`  
- `"ZJU"`: (**only available for [sub-conv-4-ZJU](https://github.com/Geniucker/sub-conv-4-ZJU)**) If this group is ZJU group. The datatype is Boolean. Possible values are `True`, `False` or don't specify this field  
- `"prior"`: What should be the default choice of this group. The datatype is `str`. If this is ZJU group, don't specify this field. Possible values are shown bellow  
  - `"DIRECT"`
  - `"PROXY"`
  - `"REJECT"`
