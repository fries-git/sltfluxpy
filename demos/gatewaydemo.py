from sltfluxpy import *
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
token = os.getenv("FLUXTOKEN")

async def connect():
    guildlist = generateguildlist(token)
    print(guildlist)
    async for data in gateway.gatewayconnect(token, guildlist):
        event = data.get("t")
        payload = data.get("d")
        if event == "MESSAGE_CREATE":
            name = payload["author"]
            name = name["username"]
            content = payload["content"]
            channel_id = payload["channel_id"]
            guild_id = payload["guild_id"]
            channel = getchanneldata(token, channel_id)
            
            if content:
                print(f"{channel["name"]}:{name} - {content}")
                if "yogurt" in content.lower():
                    await asyncio.to_thread(sendmessage, token, channel_id, "Yo, whats up.")

if __name__ == "__main__":
    asyncio.run(connect())