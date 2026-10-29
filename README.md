# Sltfluxpy
A selfbotting library to do things like dynamically set bio, and maybe allow custom client creation.  
This was created using the docs the fluxer.js provided as well as official fluxer docs.  

https://fluxer.js.org/rest/  
https://docs.fluxer.app/  
https://fluxer.app/  

# Sltfluxpy Docs
Welcome! To begin you must first install the library using:
```
pip install sltfluxpy
```  
Next, simply get your fluxer token either by the login described below or developer tool trickery. 

From [Fluxer VSCode Extension](https://marketplace.visualstudio.com/items?itemName=3urobeat.fluxer-vscode):
```
1. Log in to Fluxer at https://web.fluxer.app or your desktop app
2. Open your Developer Tools by pressing F12 (browser) or Ctrl+Shift+I (desktop app)
3. Go to the Application Tab at the top
4. Under Storage on the left, unfold Local storage and https://web.fluxer.app
5. Find the entry token in the table on the right and copy its value flx_abcdefg...
```

## How to Use
*Note that things like email/password should be in the .env file.*  
*To set token use `settoken(token)`*

### Login:
-# **Note that login is considered a currently "dangerous" function that results in hard ratelimiting and I have to fix it.**

```py
from sltfluxpy import login

login = login(email, password)
usertoken = login["token"]
# Returns token as a string from the login dict.
...
```
### Gateway:

```py
import asyncio
from sltfluxpy import login, sendmessage, generateguildlist, gateway, getchanneldata

async def connect():
    guildlist = generateguildlist(token)
    print(guildlist)
    async for data in gateway.gatewayconnect(token, guildlist):
        event = data.get("t")
        payload = data.get("d")
        ...

if __name__ == "__main__":
    asyncio.run(connect())
```