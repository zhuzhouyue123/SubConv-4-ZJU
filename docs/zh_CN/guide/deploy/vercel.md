# 在 Vercel 上部署

## 要求：
- 一个域名（由于 Vercel 的域名被 DNS 污染，因此您需要自己的域名）。不必担心，您可以免费获得域名。  
- 一个 Vercel 账户（我们将会在 Vercel 上部署）  

## 如何获得免费的二级域名
如果您有自己的域名，您可以跳过这一步。  
总共您只需要一个二级域名  
以下是提供免费域名服务的列表：[here](https://free-for.dev/#/?id=domain)  
用 <https://is-an.app>  
首先进入他们的 [仓库](https://github.com/tarampampam/free-domain#show-to-get-one)  
阅读 "How to get one?" 并按照步骤操作  
对于域名的DNS记录，仅需要设置CNAME记录到`cname.vercel-dns.com`  
但是**注意**，您应该将"proxy"设置为false  
<img src="https://user-images.githubusercontent.com/61449208/217124134-30016266-f037-4c79-87fe-ef1f693d01f3.png" width=600rem>  
example: suppose you need `example.is-an.app`  
```json
{
  "$schema": "../schemas/domain.schema.json",
  "description": "<describe your project in this field>",
  "domain": "is-an.app",
  "subdomain": "example",
  "owner": {
    "email": "<your email>"
  },
  "record": {
    "CNAME": "cname.vercel-dns.com"
  },
  "proxy": false
}
```

## 步骤
### 启用 Actions
1. Fork 这个仓库。按钮在仓库页面的右上角。你可以在新标签页中打开它。  
2. 切换到 "Actions" 菜单并启用它。然后手动触发一次 action 来缓存规则。（通常你以后不需要再这么做了）
   <img src="https://github.com/SubConv/SubConv/assets/61449208/2653bd8d-3750-4d1d-a587-1d806293239b" width=600rem>  
   <img src="https://github.com/SubConv/SubConv/assets/61449208/e30952b0-4217-4d4b-b922-4ff907d4f45e" width=600rem>    

### 部署 SubConv
然后你应该在 Vercel 上部署它，并添加你自己的域名（我称之为 sun-conv 的域名）。如果你熟悉 Vercel，可以跳过这部分。  
  然后登录 Vercel。如果你没有账号，请注册一个。  
  <img src="https://user-images.githubusercontent.com/61449208/215020343-73b16ca4-f7da-4fd1-93e5-4079ae2e000b.png" width=600rem>  
  点击 "Add New ..." 按钮，选择 "Project"  
  如果这是你第一次使用 vercel，你将被要求链接到一个 git 服务，选择 GitHub 并完成授权。  
  点击项目右侧的 "import" 按钮，克隆 https://github.com/SubConv/SubConv  
  <img src="https://user-images.githubusercontent.com/61449208/227724506-e21e3d29-1ab7-4666-8196-73245e771013.png" width=600rem>  
  然后点击 "Deploy" 按钮，等待部署完成。  
  点击 "Continue to dashboard" 按钮，进入仪表盘。  
  点击 "View Domain" 并添加你自己的域名。别忘了根据 Vercel 的指示为你的域名添加 CNAME 记录。  
  <img src="https://user-images.githubusercontent.com/61449208/215022208-f1f4e13b-ba79-47e0-bf94-1b2f050c741f.png" width=600rem>  

## 完成
