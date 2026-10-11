import requests
from datetime import datetime, timedelta, timezone

def changestatus(token, status, expirehours):
    expires_at = (datetime.now(timezone.utc) + timedelta(hours=expirehours)).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    response = requests.patch("https://web.fluxer.app/api/v1/users/@me/settings",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"},json={"custom_status": {"text": status,"expires_at": expires_at,}},timeout=10,)

    response.raise_for_status()
    return(status)

def getuser(token, id):
    response = requests.get(f"https://web.fluxer.app/api/v1/users/{id}",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"})
    response.raise_for_status()
    return(response.json())

# def login(email, password):
    response = requests.post("https://web.fluxer.app/api/v1/auth/login", headers={"Content-Type": "application/json", "Origin": "https://web.fluxer.app"}, json={"email": email,"password": password})
    return(response.json())

def sendmessage(token, channelid, content):
    response = requests.post(f"https://web.fluxer.app/api/v1/channels/{channelid}/messages", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"}, json={"content":content})
    return(response.json())