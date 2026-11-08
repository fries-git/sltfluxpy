import requests
from . import config
from datetime import datetime, timedelta, timezone

def guilduser(guild_id, user_id):
    token = config.token
    api = config.api
    response = requests.get(f"{api}/guilds/{guild_id}/members/{user_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def timeoutmember(guild_id, user_id, hours, reason):
    token = config.token
    api = config.api
    timestamp = (datetime.now(timezone.utc) + timedelta(hours=hours)).isoformat().replace("+00:00", "Z")
    js = {"communication_disabled_until": timestamp,"timeout_reason": reason}
    response = requests.patch(f"{api}/guilds/{guild_id}/members/{user_id}", json=js, headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def permabanmember(guild_id, user_id, reason):
    token = config.token
    api = config.api
    js = {"reason": reason}
    response = requests.put(f"{api}/guilds/{guild_id}/bans/{user_id}", json=js, headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())