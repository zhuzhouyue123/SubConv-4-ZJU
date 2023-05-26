# Deploy on Vercel

## Requirements:
- your own domain (the DNS resolution of vercel's domain is polluted so you have to use your own domain). Don't be worried about this, you can get one for free.  
- a vercel account (we will deploy on vercel)  

## How to get a free subdomain
If you have your own domain, skip this.  
In total you need only 1 subdomains  
Here is a list of services that provide free domains: [here](https://free-for.dev/#/?id=domain)  
Take <https://is-an.app/> for example  
First go to their [repo](https://github.com/tarampampam/free-domains#how-to-get-one)  
Read "How to get one" and follow the instruction. 
As for `"record"`, you should only set `"CNAME"` to `"cname-china.vercel-dns.com"`  
But **notice** that you should configure "proxy" to false  
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
## Steps
### Enable Actions
1. Fork this repo. The button is on the up-right side of repo page. You can open it in the new page.  
2. switch into "Actions" menu and enable it. Then manually trigger the action for the first time to cache the rules. (Normally you don't need to do this later anymore)
   <img src="https://github.com/Geniucker/sub-conv/assets/61449208/2653bd8d-3750-4d1d-a587-1d806293239b" width=600rem>
   <img src="https://github.com/Geniucker/sub-conv/assets/61449208/e30952b0-4217-4d4b-b922-4ff907d4f45e" width=600rem>  

### Deploy sub-conv
Then you should deploy this on Vercel and add you own domain (I call this **sun-conv's domain**). If you are familiar with Vercel, go ahead and skip this part.  
  Then log in [Vercel](https://vercel.com). If you don't have an account plz register one.  
  <img src="https://user-images.githubusercontent.com/61449208/215020343-73b16ca4-f7da-4fd1-93e5-4079ae2e000b.png" width=600rem>  
  Click "Add New ..." button and choose "Project"  
  Then if it's the first time to use vercel, you'll be asked to link to a git service, choose GitHub and finish the authorization.  
  Click the "import" button at the right of the project you clone  https://github.com/Geniucker/sub-conv/
  <img src="https://user-images.githubusercontent.com/61449208/227724506-e21e3d29-1ab7-4666-8196-73245e771013.png" width=600rem>  
  Then click the "Deploy" button and wait until deploy is completed.  
  Click the "Continue to dashboard" button and get into dashboard.  
  Click "View Domain" and add your own domain. Don't forget to add a CNAME record according to vercel's instruction to your domain.  
  <img src="https://user-images.githubusercontent.com/61449208/215022208-f1f4e13b-ba79-47e0-bf94-1b2f050c741f.png" width=600rem>  
  
## Finish
