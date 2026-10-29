import requests
from . import config
from datetime import datetime, timedelta, timezone

def guilduser(guild_id, user_id):
    token = config.token
    response = requests.get(f"https://web.fluxer.app/api/v1/guilds/{guild_id}/members/{user_id}", headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())

def timeoutmember(guild_id, user_id, hours, reason):
    token = config.token
    timestamp = (datetime.now(timezone.utc) + timedelta(hours=hours)).isoformat().replace("+00:00", "Z")
    js = {"communication_disabled_until": timestamp,"timeout_reason": reason}
    response = requests.patch(f"https://web.fluxer.app/api/v1/guilds/{guild_id}/members/{user_id}", json=js, headers={"Authorization": token,"Content-Type": "application/json", "Origin":"https://web.fluxer.app"})
    return(response.json())