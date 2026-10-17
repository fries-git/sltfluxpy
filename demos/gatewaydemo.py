from sltfluxpy import gateway, sendmessage, getchanneldata
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
token = os.getenv("FLUXTOKEN")

guildids = ["1472374293066228010", "1473443172612104279"]

async def connect():
    async for data in gateway.gatewayconnect(token, guildids):
        opcode = data.get("op")
        event = data.get("t")
        payload = data.get("d")
        if event == "MESSAGE_CREATE":
            name = payload["author"]
            name = name["username"]
            content = payload["content"]
            channel_id = payload["channel_id"]
            guild_id = payload["guild_id"]
            channel = getchanneldata(token, channel_id)
            
            if guild_id in guildids:
                if content:
                    print(f"{channel["name"]}:{name} - {content}")
                    if content == "fr&ping":
                        await asyncio.to_thread(sendmessage, token, channel_id, "Pong!")

if __name__ == "__main__":
    asyncio.run(connect())