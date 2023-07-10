import websockets
import asyncio
import json

def process_msg(data):
    url = "ws://localhost:8000/graphql"
    v = data.get('payload').get('data').get('temperature')
    query_string = """
mutation { createTemperature(value: %s) { ok }}
    """ % v
    start = {
        "type": "start",
        "payload": { "query": query_string }
    }
    print(start)
    '''
    async with websockets.connect(url, subprotocols=["graphql-ws"]) as websocket:
        await websocket.send(json.dumps(start))
    '''

async def subscribe_to_data():
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

asyncio.run(subscribe_to_data())