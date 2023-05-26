# 为什么使用 sub-conv

现在已经有很多 Clash 的订阅转换器了，为什么还要使用 sub-conv 呢？换句话说，sub-conv 有什么优点呢？  

## 易于免费部署
subconverter 是用 C++ 开发的，因此难以部署在 Serverless 平台上。而 sub-conv 是用 Python 开发的，因此可以轻松部署在 Vercel 上。只要您有一个域名（可以免费获得），您就可以免费部署它。  

## 安全
它部署在您自己的 Vercel 或 VPS 上，因此没有其他人可以看到您的数据。  

## 使用 proxy-provider 实现自动更新
其他订阅转换器通常不会实现自动更新。因此，如果您想在使用 Clash 核心时更新代理，您必须编写脚本。但是如果您使用 sub-conv，您就不需要这样做，因为 sub-conv 使用 proxy-provider（Clash 的一个特性）来实现自动更新。  

## 易于定制
您可以通过修改配置文件来自定义规则集。同时，您也可以通过修改源代码来进行更深度的自定义。因为使用的语言 Python 非常接近自然语言。 
