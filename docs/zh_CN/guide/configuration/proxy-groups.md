# Proxy Groups
有一些固定的组，包括 `🚀 节点选择`, `🚀 手动切换`, `♻️ 自动选择`, `🔯 故障转移` 和地区组，如 `🇭🇰 香港节点`。其他组可以通过配置文件 `config.py` 进行自定义。您还可以自定义规则组。例如，您可以自定义规则组。如您所见，配置文件是Python语法。我将在下面介绍用法。  

## 自定义 proxy-groups
一个有效的配置文件应该像这样：  
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
支持两种类型的组：`load-balance` 和 `select`  
对于 `load-balance` 组，有3个字段：  
- `"name"`: 组的名称，数据类型应该是 `str`  
- `"type"`: 应为 `"load-balance"`，数据类型是 `str`  
- `"region"`: 您想要添加到一个负载均衡组的地区。如果未指定，则所有代理都将出现。此字段的数据类型应为 `list`，`list` 中每个元素的类型应为 `str`。可能的值为 `"HK"`，`"TW"`，`"KR"`，`"JP"`，`"US"`，`"SG"`  

对于 `select` 组，有4个字段：  
- `"name"`: 组的名称，数据类型应该是 `str`  
- `"type"`: 应为 `"select"`，数据类型是 `str`  
- `"ZJU"`: (**仅对 [sub-conv-4-ZJU](https://github.com/Geniucker/sub-conv-4-ZJU)有效**) 是否是ZJU分组。数据类型是 `bool`。可能的值为 `True`、`False`和缺省  
- `"prior"`: 这个组的默认选择是什么。数据类型为 str。如果这是 ZJU 组，请不要指定该字段。可能的取值如下所示  
  - `"DIRECT"`  
  - `"REJECT"`  
  - `"PROXY"`
