# Why SubConv

There are many subscription converters for Clash, but why should you choose SubConv? In other words, what are the advantages of SubConv?  

## Easy to Deploy for free
subconverter is developed in C++, which is not easy to deploy as serverless functions. SubConv is written in Python. Thus, it's easy to deploy it on Vercel. As long as you have a domain (can be got for free), you can deploy it for free.  

## Safe
It's deployed on your own Vercel or VPS, so nobody else can see your data.  

## Using proxy-provider to implement auto-update
Other subscription converters don't usually implement auto-update. So if you want to update the proxies while using clash core, you have make efforts to write scripts. But if you use SubConv, you don't need to do that because SubConv uses proxy-provider (a feature of Clash) to implement auto-update.  

## Easy to Customize
You can customize the rule sets by modifying the config file.  
It's also easy to do some further modifications by modifying the source code because it's written in Python which is like natural language.  
