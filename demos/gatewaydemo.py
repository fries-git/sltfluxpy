from sltfluxpy import gateway, sendmessage
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
token = os.getenv("FLUXTOKEN")

async def connect():
    async for data in gateway.gatewayconnect(token):
        opcode = data.get("op")
        event = data.get("t")
        payload = data.get("d")
        if event == "MESSAGE_CREATE":
            name = payload["author"]
            name = name["username"]
            content = payload["content"]
            channel_id = payload["channel_id"]
            print(f"{name} - {content}")
            if content == "fr!ping":
                await asyncio.to_thread(sendmessage, token, channel_id, "Pong!")

if __name__ == "__main__":
    asyncio.run(connect())