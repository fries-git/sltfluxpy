import requests

def sendmessage(token, channel_id, content):
    response = requests.post(f"https://web.fluxer.app/api/v1/channels/{channel_id}/messages", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"}, json={"content":content})
    return(response.json())

def editmessage(token, channel_id, message_id, content):
    response = requests.patch(f"https://web.fluxer.app/api/v1/channels/{channel_id}/messages/{message_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"}, json={"content":content})
    return(response.json())

def deletemessage(token, channel_id, message_id):
    response = requests.delete(f"https://web.fluxer.app/api/v1/channels/{channel_id}/messages/{message_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def getmessage(token, channel_id, message_id):
    response = requests.get(f"https://web.fluxer.app/api/v1/channels/{channel_id}/messages/{message_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def react(token, channel_id, message_id, emoji):
    response = requests.delete(f"https://web.fluxer.app/api/v1/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response)

def getmessages(token, channel_id, count):
    response = requests.get(f"https://web.fluxer.app/api/v1/channels/{channel_id}/messages",headers={"Authorization": token,"Origin": "https://web.fluxer.app"},params={"limit": count})
    return response.json()

def getmessagesbeforeid(token, channel_id, count, before_id):
    response = requests.get(f"https://web.fluxer.app/api/v1/channels/{channel_id}/messages",headers={"Authorization": token,"Origin": "https://web.fluxer.app"},params={"before": before_id, "limit": count})
    return response.json()