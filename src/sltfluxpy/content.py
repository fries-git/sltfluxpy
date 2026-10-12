import requests

def getemojidata(token, emoji_id):
    response = requests.get(f"https://web.fluxer.app/api/v1/emojis/{emoji_id}/metadata", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})    
    return(response.json())