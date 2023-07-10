import websockets
import requests
import asyncio
import json
from time import sleep

# this will queue NUM_RETRIES * message rate before exiting
NUM_RETRIES = 100

def process_msg(data) -> None:
    pub_url: str = "http://localhost:8000/graphql"
    v: str = data.get("payload").get("data").get("temperature")
    query_string: str = "mutation { createTemperature(value: %s) { ok }}" % v
    payload: dict = {"query": query_string}
    for _ in range(NUM_RETRIES):
        try:
            response = requests.post(pub_url, json=payload)
            if response.status_code == 200:
                print(payload)
                break
        except requests.exceptions.ConnectionError:
            # woo hoo! thatsa fast output! cheat with sleep.
            # nice surprise is the receive buffer comes for free
            # so we get a small queue in memory when the app server is down.
            # When it starts the subscriber will catch up.
            sleep(1)
            print("Connection error, retrying...")
            pass

async def subscribe_to_data() -> None:
    sub_url: str = "ws://localhost:1000/graphql"
    start: dict = {
        "type": "start",
        "payload": {"query": "subscription { temperature }"},
    }
    async with websockets.connect(sub_url, subprotocols=["graphql-ws"]) as websocket:
        await websocket.send(json.dumps(start))
        while True:
            data: str = await websocket.recv()
            process_msg(json.loads(data))


asyncio.run(subscribe_to_data())
