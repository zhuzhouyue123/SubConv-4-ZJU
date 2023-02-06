# Subscription Converter
(for ZJUers)
这是一个Clash订阅转换接口  
demo: <https://sub-converter.geniucker.top>  
如果是试用可以直接点进demo看用法  
## 功能
- 大体基于 ACL 的规则（包括了ZJU专用规则）  
- 基于 Provider 的节点自动更新  
- 对[ZJU Connect](https://github.com/Mythologyli/ZJU-Connect/)的支持  
- 剩余流量和总流量的显示（需要你的机场和你用的Clash同时支持，已知Clash for Windows, Clash Verge, Stash, Clash Meta for Android等已支持）  
## 说明
~~如需使用请自行部署（因为vercel每个人的用量是有限的，太多人用会挂）~~新开了个vercel号用于demo。你可以用上面的demo（不保证可用性，但基本上不会出啥问题），也可以自己部署，推荐部署在vercel，一是免费，二是规则缓存在仓库里，更新的时候Vercel会自动更新，如确实想部署到服务器，可以先看[Wiki](https://github.com/Geniucker/sub-conv/wiki)里部署到Vercel的教程，然后自行解决规则更新问题，当然你可以联系我问我一些注意事项  
这一页只是简单说明，详细用法和**部署方法**请看[Wiki](https://github.com/Geniucker/sub-conv/wiki) (英文写的)  
~~本接口适用于一元机场的订阅转换（大概率不适用于别的机场）~~ 现理论上适配所有机场，只需原始配置是Clash配置即可，由于使用了clash特性proxy-provider，Linux用户只需保存转换后的配置可实现自动更新节点<br>
本项目地址：<https://github.com/Geniucker/sub-conv><br>
规则来源：浙大和通用规则<https://github.com/Mythologyli/ZJU-Rule>和我的自定义规则<https://github.com/Geniucker/sub-conv/tree/custom-rules><br>
具体规则参见`modules/ruleList.py`和`cache.py`文件<br>

## 食用方法
打开部署的链接或者上面给的demo，填如对应信息，点击确认生成，即可生成新的订阅链接，点击复制即可复制到剪贴板。  

## 安全性问题
本接口需要先读取你的订阅的内容再生成地区分组，该过程无任何持久化或网络发送操作，所以是安全的。您可以检查本项目的相关代码和[Proxy Provider Converter](https://github.com/qier222/proxy-provider-converter)的代码。  

## 致谢
- [ZJU-Rule](https://github.com/Mythologyli/ZJU-Rule/)
- [subconverter](https://github.com/tindy2013/subconverter)
- [Proxy Provider Converter](https://github.com/qier222/proxy-provider-converter)
