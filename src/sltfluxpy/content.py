import requests

def getemojidata(token, emoji_id):
    response = requests.get(f"https://web.fluxer.app/api/v1/emojis/{emoji_id}/metadata", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})    
    return(response.json())

def getchanneldata(token, channel_id):
    response = requests.get(f"https://web.fluxer.app/api/v1/channels/{channel_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def getguildchannels(token, guild_id):
    response = requests.get(f"https://web.fluxer.app/api/v1/guilds/{guild_id}/channels", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(sorted(response.json(), key=lambda channel: channel["position"]))

def getguilds(token):
    response = requests.get(f"https://web.fluxer.app/api/v1/users/@me/guilds", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())