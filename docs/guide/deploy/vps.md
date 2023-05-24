# Deploy on VPS or PC
Here I suppose you're using Linux server.  

## Steps
1. Fork this repo to your own account.  
2. switch into "Actions" menu and enable it. Then manually trigger the action for the first time to cache the rules. (Normally you don't need to do this later anymore)
   <img src="https://github.com/Geniucker/sub-conv/assets/61449208/2653bd8d-3750-4d1d-a587-1d806293239b" width=600rem>
   <img src="https://github.com/Geniucker/sub-conv/assets/61449208/e30952b0-4217-4d4b-b922-4ff907d4f45e" width=600rem>  
3. Use you package manager to install `python3`, `python3-pip` and `git` on your VPS. And it's ***recommended to use a reverse proxy*** to provide https. I won't talk about this here.  
4. Clone your forked repo to your VPS and `cd` into it. (If you like, you can create virtual environment using `env`)  
5. `pip3 install -r requirements.txt` to install dependencies.  
6. `chmod +x api.py` to give permission for execution  
7. `./api.py -h` or `python3 api.py -h` to see usage  
   for example, you can use `./api.py -H 127.0.0.1 -P 2534` or `python3 api.py -H 127.0.0.1 -P 2534` to specify the host and port listened. If all parameters are omitted, the host will be 0.0.0.0 and port will be 443  
   > ***Attention***: If you're not using privileged user, normally you are not able to bind ports under 1024. It's recommended to use high ports or you can use `setcap` to give python permission to bind lower ports.  
8. User reverse proxy (optional)

## After Deployment
The GitHub Actions will cache rules to your repo regularly, but it won't be synchronized into your VPS automatically. So you may need to execute `git pull` manually or you can use script to finish this automatically  

## Enjoy
