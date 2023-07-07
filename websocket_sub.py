import websockets
import asyncio
import json

def process_msg(data):
    print(data)

async def capture_data():
    url = "ws://localhost:1000/graphql"
    start = {
        "type": "start",
        "payload": {"query": "subscription { temperature }" }
    }
    async with websockets.connect(url, subprotocols=["graphql-ws"]) as websocket:
        await websocket.send(json.dumps(start))
        while True:
            data = await websocket.recv()
            process_msg(json.loads(data))

asyncio.run(capture_data())