import asyncio
from websockets.asyncio.client import connect
import json

async def gatewayconnect(token):
    async with connect("wss://gateway.fluxer.app?v=1&encoding=json", max_size=10 * 1024 * 1024) as websocket:
        authobj = {"op": 2,"d": {"token": token,"properties": {"os": "Linux","browser": "Fluxer Client","device": "desktop"}}}
        await websocket.send(json.dumps(authobj))

        queue = asyncio.Queue()

        async def receiver():
            async for message in websocket:
                await queue.put(json.loads(message))

        async def heartbeat():
            while True:
                await asyncio.sleep(41.25)
                await websocket.send(json.dumps({"op": 1,"d": 42}))

        heartbeat_task = asyncio.create_task(heartbeat())
        receiver_task = asyncio.create_task(receiver())

        try:
            while True:
                message = await queue.get()
                yield message
                queue.task_done()
        finally:
            heartbeat_task.cancel()
            receiver_task.cancel()