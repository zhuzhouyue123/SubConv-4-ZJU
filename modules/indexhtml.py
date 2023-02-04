"""
This module contains the html code of mainpage
"""


content = """
<meta charset="utf-8">
# 使用说明
~~本接口适用于一元机场的订阅转换（大概率不适用于别的机场）~~理论上适配所有Clash机场，由于使用了clash特性proxy-provider，Linux用户只需保存转换后的配置可实现自动更新节点<br>
本项目地址：<https://github.com/Geniucker/sub-conv><br>
规则来源：<https://github.com/Mythologyli/ZJU-Rule>和<https://github.com/Geniucker/sub-conv/tree/custom-rules><br>
具体规则参见`modules/ruleList.py`和`cache.py`文件<br>

## 接口语法
目前本接口仅支持get请求<br>
接口链接：<{}sub><br>
支持的参数有:<br>
  1. `url`：值为你的一元机场订阅链接<br>
  2. `interval`：（可选）值为自动拉取节点的时间间隔，单位为秒，若无此参数则默认为600<br>
    若是你一般一直把clash挂在后台（例如挂在软路由、NAS，或者长期挂后台），建议此项设置大一点，例如3600，以减小订阅服务器负载<br>
    若是一般只是短时间使用时打开clash，建议设置小一点，比如300或600，防止无法及时拉取节点
  3. `zjuport'：（可选）值为[ZJU Connect](https://github.com/Mythologyli/ZJU-Connect/)暴露的端口，若不使用则不填
示例：<br>
不指定时间间隔
```
{}sub?url=<订阅链接>
```
指定时间间隔<br>
```
{}sub?url=<订阅链接>&interval=<时间间隔>
```
使用[ZJU Connect](https://github.com/Mythologyli/ZJU-Connect/)<br>
```
https://example.com/sub?url=<订阅链接>&zjuport=<端口>
```

<!-- Markdeep: --><style class="fallback">body{{visibility:hidden;white-space:pre;font-family:monospace}}</style><script src="/static/js/markdeep.min.js" charset="utf-8"></script><script>window.alreadyProcessedMarkdeep||(document.body.style.visibility="visible")</script>
"""
