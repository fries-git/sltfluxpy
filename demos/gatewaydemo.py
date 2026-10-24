from sltfluxpy import login, sendmessage, generateguildlist, gateway, getchanneldata
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
email, pwrd = os.getenv("EMAIL"), os.getenv("PASSWORD")
token = login(email, pwrd)["token"]

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
                if "slab" in content.lower():
                    if not "return the slab..." in content.lower():
                        await asyncio.to_thread(sendmessage, token, channel_id, "-# return the slab...")

if __name__ == "__main__":
    asyncio.run(connect())