import requests
from datetime import datetime, timedelta, timezone
import base64
from . import config
from .log import *

advancedlog = config.advanced_logging

def changestatus(status, expirehours):
    token = config.token
    expires_at = (datetime.now(timezone.utc) + timedelta(hours=expirehours)).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    response = requests.patch("https://web.fluxer.app/api/v1/users/@me/settings",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"},json={"custom_status": {"text": status,"expires_at": expires_at}},timeout=10)
    return(response.json())

def changedisplay(name):
    token = config.token
    response = requests.patch("https://web.fluxer.app/api/v1/users/@me",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"},json={"global_name": name},timeout=10)
    return(response.json())

def changebio(bio):
    token = config.token
    response = requests.patch("https://web.fluxer.app/api/v1/users/@me",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"},json={"bio": bio},timeout=10)
    return(response.json())

def changeaccentcolor(hexcolor):
    token = config.token
    color = int(hexcolor.replace("#", ""), 16)
    response = requests.patch("https://web.fluxer.app/api/v1/users/@me",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"},json={"accent_color": color},timeout=10)
    return(response.json())

def changepronouns(pronouns):
    token = config.token
    response = requests.patch("https://web.fluxer.app/api/v1/users/@me",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"},json={"pronouns": pronouns},timeout=10)
    return(response.json())

def getuser(id):
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/users/{id}",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"})
    return(response.json())

def getuserpfp(id):
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/users/{id}",headers={"Authorization":token, "Content-Type": "application/json","Origin": "https://web.fluxer.app"})
    response = response.json()
    success(response)
    response = response["avatar"]
    return f"https://fluxerusercontent.com/avatars/{id}/{response}.png"

def changepfp(url):
    token = config.token
    try:
        image = requests.get(url)
        image.raise_for_status()
    except:
        return("Image Fetch Error")

    mimetype = image.headers.get("Content-Type", "").split(";")[0]
    if not mimetype.startswith("image/"):
        return("URL did not return an image")

    image_data = base64.b64encode(image.content).decode("utf-8")
    response = requests.patch("https://api.fluxer.app/v1/users/@me",headers={"Authorization": token,"Content-Type": "application/json"},json={"avatar": f"data:{mimetype};base64,{image_data}"})

    return response

def getnote(userid):
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/users/@me/notes/{userid}",headers={"Authorization": token,"Content-Type": "application/json","Origin": "https://web.fluxer.app"})
    return(response.json())