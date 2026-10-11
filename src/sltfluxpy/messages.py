import requests
from datetime import datetime, timedelta, timezone

def sendmessage(token, channelid, content):
    response = requests.post(f"https://web.fluxer.app/api/v1/channels/{channelid}/messages", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"}, json={"content":content})
    return(response.json())