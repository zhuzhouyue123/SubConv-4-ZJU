# Cache rules automatically
I use rule cache mainly to accelerate the speed.  

But to keep the cache up to date, I use GitHub Action to generate the cache regularly.  

The config for rule cache can be seen in `.github/workflows/update-rules.yml`.  

You can modify the 7th line (`- cron: "0 16 1/7 * *"`) to change the update frequency. The default is to update the cache every 7 days.  
