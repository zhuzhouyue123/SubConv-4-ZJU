# 在 VPS 或 PC 上部署
这里我假设你使用的是 Linux 服务器。  

## 步骤
1. Fork 这个仓库到你自己的账户。  
2. 切换到 "Actions" 菜单并启用它。然后手动触发一次 action 来缓存规则。（通常你以后不需要再这么做了）
   <img src="https://github.com/SubConv/SubConv/assets/61449208/2653bd8d-3750-4d1d-a587-1d806293239b" width=600rem>  
   <img src="https://github.com/SubConv/SubConv/assets/61449208/e30952b0-4217-4d4b-b922-4ff907d4f45e" width=600rem>    
3. 使用你的包管理器在你的 VPS 上安装 `python3`、`python3-pip` 和 `git`。并且***推荐使用反向代理***来提供 https。我不会在这里讨论这个。  
4. 克隆你 fork 的仓库到你的 VPS 并进入它。（如果你喜欢，你可以使用 `env` 创建虚拟环境）  
5. `pip3 install -r requirements.txt` 来安装依赖。  
6. `chmod +x api.py` 来给予执行权限  
7. `./api.py -h` 或 `python3 api.py -h` 来查看用法  
   例如，你可以使用 `./api.py -H 127.0.0.1 -P 2534' 或 'python3 api.py -H 127.0.0.1 -P 2534` 来指定监听的主机和端口。如果所有参数都被省略，host 将会是0.0.0.0，端口将会是443'  
    > ***注意***：如果你不是使用特权用户，通常你是不能绑定 1024 以下的端口的。推荐使用高端口或者你可以使用 `setcap` 来给 python 绑定低端口的权限。  
8. 使用反向代理（可选）  

## 部署后
GitHub Actions 会定期缓存规则到你的仓库，但它不会自动同步到你的 VPS。所以你可能需要手动执行 `git pull` 或者你可以使用脚本来自动完成这个步骤。  

## 尽情享受吧
