# Subscription Converter
![license](https://img.shields.io/github/license/geniucker/sub-conv) ![last commit](https://img.shields.io/github/last-commit/geniucker/sub-conv)  
这个项目是面向所有Clash用户的订阅转换，如果你需要ZJU专版，请移步[sub-conv 4 ZJU](https://github.com/geniucker/sub-conv-4-ZJU)
这是一个Clash订阅转换接口(仅提供试用，不保证安全性及可用性)  
demo: <https://sub-converter.geniucker.top>  
如果是试用可以直接点进demo看用法  
> ***有能力请自行部署，因为vercel仓库所有者可以通过日志看到一个小时内发生错误的那次请求的请求参数***，当然我不会闲着没事去看，但请自行评估风险

## 功能
- 支持Clash配置和V2ray格式的base64链接（即原始订阅不一定是Clash）  
- 一个可以勉强能看的订阅转换 Web-UI (感谢 [@Musanico](https://github.com/musanico))  
- 大体基于 ACL 的规则  
- 基于 Provider 的节点自动更新  
- （为土豪）多机场用户提供了支持  
- 剩余流量和总流量的显示（单机场的时候才有用，需要你的机场和你用的Clash同时支持，已知Clash for Windows, Clash Verge, Stash, Clash Meta for Android等已支持）  
- 实现了 clash 订阅转换 proxy-provider 的 api, (一般人也不会去用吧), 不再依赖 [Proxy Provider Converter](https://github.com/qier222/proxy-provider-converter) , 用法`<网页根目录>/provider?url=<你的订阅>`,例如上面给出的示例,地址为`https://sub-converter.geniucker.top/provider?url=<你的订阅>`,`<你的订阅>`自行替换  
- 支持配置文件 (`config.py`，之后说不定会写subconverter配置到本项目的转换)  

## 部署
~~如需使用请自行部署（因为vercel每个人的用量是有限的，太多人用会挂）~~ 新开了个vercel号用于demo。你可以用上面的demo（不保证可用性，但基本上不会出啥问题），也可以自己部署，推荐部署在vercel，一是免费，二是规则缓存在仓库里，更新的时候Vercel会自动更新，如确实想部署到服务器，可以先看[Wiki](https://github.com/Geniucker/sub-conv/wiki)里部署到Vercel的教程，然后自行解决规则更新问题，当然你可以联系我问我一些注意事项  
这一页只是简单说明，详细用法和**部署方法**请看[Wiki](https://github.com/Geniucker/sub-conv/wiki) (英文写的)  

##说明
~~本接口适用于一元机场的订阅转换（大概率不适用于别的机场）~~ 现理论上适配所有机场，由于使用了clash特性proxy-provider，Linux用户只需保存转换后的配置可实现自动更新节点(不需要自动更新的脚本，是clash核心本身支持的)<br>
本项目地址：<https://github.com/Geniucker/sub-conv><br>
规则来源：通用规则<https://github.com/Mythologyli/ZJU-Rule><br>
代码直接读取的规则具体参见`modules/ruleList.py`<br>

## 食用方法
打开部署的链接或者上面给的demo，填如对应信息，点击确认生成，即可生成新的订阅链接，点击复制即可复制到剪贴板。  

## 安全性问题
本接口需要先读取你的订阅的内容再生成地区分组，该过程无任何持久化或网络发送操作，所以是安全的。您可以检查本项目的相关代码  
> 但是Vercel仓库所有者可以通过日志看到一个小时内发生错误的那次请求的请求参数，所以请自行部署或使用可信的人的部署。  

## 为本项目贡献
欢迎 issue 和 PR。如果要提pr请从main分支开新分支然后提pr到dev分支，或者也可以先把main合并到dev然后在dev里改，最后提pr到dev  

## 致谢
- [ZJU-Rule](https://github.com/Mythologyli/ZJU-Rule/)  
- [subconverter](https://github.com/tindy2013/subconverter)  
- [Clash.Meta](https://github.com/MetaCubeX/Clash.Meta)  
- ~~[Proxy Provider Converter](https://github.com/qier222/proxy-provider-converter)~~  

## 许可证
本项目采用 [MIT License](https://github.com/Geniucker/sub-conv/blob/main/LICENSE) 分发  