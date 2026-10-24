## All functions
```
changeaccentcolor(token, hexcolor)  
changebio(token, bio)  
changedisplay(token, name)  
changepfp(token, url)  
changepronouns(token, pronouns)  
changestatus(token, status, expirehours)  
deletemessage(token, channel_id, message_id)  
editmessage(token, channel_id, message_id, content)  
gatewayconnect(token, subscriptions)  
generateguildlist(token)  
getchanneldata(token, channel_id)  
getemojidata(token, emoji_id)  
getgateway(token) *(seems to be busted which is crazy considering its like the simplest thing)*
getguildchannels(token, guild_id)  
getguilds(token)  
getmessage(token, channel_id, message_id)  
getmessages(token, channel_id, count)  
getmessagesbeforeid(token, channel_id, count, before_id)  
getnote(token, userid)  
getuser(token, id)  
getuserpfp(token, id)  
github()  
lazyrequest(websocket, message)  
login(email, password) *(does not work due to captcha)*
react(token, channel_id, message_id, emoji) *(seems to be broken idk)*
sendmessage(token, channel_id, content)  
```

## How to Use
*Note that things like email/password should be in the .env file.*  

### Login:

```py
from sltfluxpy import login

login = login(email, password)
usertoken = login["token"]
# Returns token as a string from the login dict.
...
```
### Gateway:

```python
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