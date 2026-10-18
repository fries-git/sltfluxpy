import asyncio
from websockets.asyncio.client import connect
import json

async def gatewayconnect(token, subscriptions):
    global websocket
    async with connect("wss://gateway.fluxer.app?v=1&encoding=json", max_size=10 * 1024 * 1024) as websocket:
        print("✔ Connecting...")
        authobj = {"op": 2,"d": {"token": token,"properties": {"os": "Linux","browser": "Fluxer Client","device": "desktop"}}}
        await websocket.send(json.dumps(authobj))

        queue = asyncio.Queue()

        async def receiver():
            async for message in websocket:
                await queue.put(json.loads(message))

        async def heartbeat():
            while True:
                await websocket.send(json.dumps({"op": 1,"d": 42}))
                await asyncio.sleep(41.25)
        
        heartbeat_task = asyncio.create_task(heartbeat())
        receiver_task = asyncio.create_task(receiver())
        for id in subscriptions:
            await lazyrequest(websocket, id)
            await asyncio.sleep(.1)
        print("✔ Done subscribing to channels, websocket ready!")
        try:
            while True:
                message = await queue.get()
                yield message
                queue.task_done()
        finally:
            heartbeat_task.cancel()
            receiver_task.cancel()

async def lazyrequest(websocket, serverid):
    await websocket.send(json.dumps({"op": 14,"d": {"subscriptions": {str(serverid): {"active": True,"typing": True}}}}))