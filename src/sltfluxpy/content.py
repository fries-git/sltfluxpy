import requests
from . import config

advancedlog = config.advanced_logging

def getemojidata(emoji_id):
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/emojis/{emoji_id}/metadata", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})    
    return(response.json())

def getchanneldata(channel_id):
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/channels/{channel_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def getguildchannels(guild_id):
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/guilds/{guild_id}/channels", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(sorted(response.json(), key=lambda channel: channel["position"]))

def getguilds():
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/users/@me/guilds", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def generateguildlist():
    token = config.token
    return {"op": 14,"d": {"subscriptions":{"0": {"active": True, "sync": False, "typing": False}, **{str(guild["id"]): {"active": True,"sync": False,"typing": False}for guild in getguilds()}}}}

def getgateway():
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/gateway/bot",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"})
    return (response.json())