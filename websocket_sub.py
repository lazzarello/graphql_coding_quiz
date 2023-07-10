import websockets
import requests
import asyncio
import json

def process_msg(data) -> None:
    pub_url: str = "http://localhost:8000/graphql"
    v: str = data.get('payload').get('data').get('temperature')
    query_string: str = "mutation { createTemperature(value: %s) { ok }}" % v
    payload: dict = { "query": query_string }
    print(payload)
    requests.post(pub_url, json=payload)

async def subscribe_to_data() -> None:
    sub_url: str = "ws://localhost:1000/graphql"
    start: dict = {
        "type": "start",
        "payload": {"query": "subscription { temperature }" }
    }
    async with websockets.connect(sub_url, subprotocols=["graphql-ws"]) as websocket:
        await websocket.send(json.dumps(start))
        while True:
            data: str = await websocket.recv()
            process_msg(json.loads(data))

asyncio.run(subscribe_to_data())