# 规则自动缓存
使用缓存主要是为了提高性能。  

但是为了保持缓存最新，我使用 GitHub Actions 来定期生成缓存。  

对应的配置在 `.github/workflows/update-rules.yml` 中。  

你可以修改第7行 (`- cron: "0 16 1/7 * *"`) 来修改更新频率值，默认为每7填更新一次。  
