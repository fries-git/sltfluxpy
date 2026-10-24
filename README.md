# Sltfluxpy
A selfbotting library to do things like dynamically set bio, and maybe allow custom client creation.  
This was created using the docs the fluxer.js provided as well as official fluxer docs.  
So far I've put about 10 hours into it, feels pretty good, and im liking how it works.  
The first thing I'm making is good Spotify linking program. Use premium to set status to song.  

https://fluxer.js.org/rest/  
https://docs.fluxer.app/  
https://fluxer.app/  

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