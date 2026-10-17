from sltfluxpy import getguildchannels, getmessages
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("FLUXTOKEN")
guild_id = "1472374293066228010"

channels = getguildchannels(token, guild_id)
print("CHANNELS:", repr(channels))

if channels:
    channel_id = str(channels[0]["id"])
    print("MESSAGES:", repr(getmessages(token, channel_id)))