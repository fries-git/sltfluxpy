# Sltfluxpy
A selfbotting library to do things like dynamically set bio, and maybe allow custom client creation. This is pretty much exclusively used for HTTP requests, gateway, while it does work, doesnt have the things needed to work in >100 member servers.

## Functions
changedisplay(token, name)  
changepronouns(token, pronouns)  
changestatus(token, status, expirehours)  
deletemessage(token, channelid, messageid)  
editmessage(token, channelid, messageid, content)  
gatewayconnect(token)  
getemojidata(token, emoji_id)  
getmessage(token, channelid, messageid)  
getuser(token, id)  
getuserpfp(token, id)  
github()  
login(email, password)  
react(token, channelid, messageid, emoji)  
sendmessage(token, channelid, content)  