## All functions
```
settoken(token)  
  
changeaccentcolor(hexcolor)  
changebio(bio)  
changedisplay(name)  
changepfp(url)  
changepronouns(pronouns)  
changestatus(status, expirehours)  
deletemessage(channel_id, message_id)  
docs()  
editmessage(channel_id, message_id, content)  
error(input)  
gatewayconnect(subscriptions)  
generateguildlist()  
getchanneldata(channel_id)  
getemojidata(emoji_id)  
getgateway()  
getguildchannels(guild_id)  
getguilds()  
getmessage(channel_id, message_id)  
getmessages(channel_id, count)  
getmessagesbeforeid(channel_id, count, before_id)  
getnote(userid)  
getuser(id)  
getuserpfp(id)  
github()  
lazyrequest(websocket, message)  
login(email, password)  
logout()  
logoutmanual(token)  
react(channel_id, message_id, emoji)  
readme()  
sendmessage(channel_id, content)  
success(input)  
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