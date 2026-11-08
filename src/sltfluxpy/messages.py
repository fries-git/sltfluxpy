import requests
from . import config

advancedlog = config.advanced_logging

def sendmessage(channel_id, content):
    token = config.token
    api = config.api
    if advancedlog:
        print(api)
    response = requests.post(f"{api}/channels/{channel_id}/messages", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"}, json={"content":content})
    return(response.json())

def editmessage(channel_id, message_id, content):
    token = config.token
    api = config.api
    response = requests.patch(f"{api}/channels/{channel_id}/messages/{message_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"}, json={"content":content})
    return(response.json())

def deletemessage(channel_id, message_id):
    token = config.token
    api = config.api
    response = requests.delete(f"{api}/channels/{channel_id}/messages/{message_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return("Message deleted.")

def getmessage(channel_id, message_id):
    token = config.token
    api = config.api
    response = requests.get(f"{api}/channels/{channel_id}/messages/{message_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def react(channel_id, message_id, emoji):
    token = config.token
    api = config.api
    response = requests.delete(f"{api}/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response)

def getmessages(channel_id, count):
    token = config.token
    api = config.api
    response = requests.get(f"{api}/channels/{channel_id}/messages",headers={"Authorization": token,"Origin": "https://web.fluxer.app"},params={"limit": count})
    return response.json()

def getmessagesbeforeid(channel_id, count, before_id):
    token = config.token
    api = config.api
    response = requests.get(f"{api}/channels/{channel_id}/messages",headers={"Authorization": token,"Origin": "https://web.fluxer.app"},params={"before": before_id, "limit": count})
    return response.json()