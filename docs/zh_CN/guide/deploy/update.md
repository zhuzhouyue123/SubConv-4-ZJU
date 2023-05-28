# 如何更新

## 如果部署在 Vercel 上
当你的 forked 仓库不是最新时，你可以按照下面的图片来将其与原始仓库同步：
![image](https://user-images.githubusercontent.com/61449208/241410800-0f0be65a-a459-49f6-92d3-8f8ceeb4baf5.png)
之后，Vercel 将自动重新部署。

## 如果部署在你的 VPS 上
1. 根据上述图片将你的 forked 仓库与原始仓库同步。
2. 停止 `SubConv` 的进程。
3. 在你的 VPS 中 `SubConv` 文件夹的目录下运行 `git pull`。
4. 重新启动 `SubConv`。
