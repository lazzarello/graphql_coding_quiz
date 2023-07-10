import websockets
import requests
import asyncio
import json

def process_msg(data):
    pub_url = "http://localhost:8000/graphql"
    v = data.get('payload').get('data').get('temperature')
    query_string = "mutation { createTemperature(value: %s) { ok }}" % v
    payload = { "query": query_string }
    # an HTTP POST to the pub_url with the payload as the body
    print(payload)
    requests.post(pub_url, json=payload)

async def subscribe_to_data():
    sub_url = "ws://localhost:1000/graphql"
    start = {
        "type": "start",
        "payload": {"query": "subscription { temperature }" }
    }
    async with websockets.connect(sub_url, subprotocols=["graphql-ws"]) as websocket:
        await websocket.send(json.dumps(start))
        while True:
            data = await websocket.recv()
            process_msg(json.loads(data))

asyncio.run(subscribe_to_data())