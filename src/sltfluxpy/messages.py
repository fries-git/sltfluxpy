import requests

def sendmessage(token, channelid, content):
    response = requests.post(f"https://web.fluxer.app/api/v1/channels/{channelid}/messages", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"}, json={"content":content})
    return(response.json())

def editmessage(token, channelid, messageid, content):
    response = requests.patch(f"https://web.fluxer.app/api/v1/channels/{channelid}/messages/{messageid}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"}, json={"content":content})
    return(response.json())

def deletemessage(token, channelid, messageid):
    response = requests.delete(f"https://web.fluxer.app/api/v1/channels/{channelid}/messages/{messageid}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def getmessage(token, channelid, messageid):
    response = requests.get(f"https://web.fluxer.app/api/v1/channels/{channelid}/messages/{messageid}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def react(token, channelid, messageid, emoji):
    response = requests.delete(f"https://web.fluxer.app/api/v1/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response)