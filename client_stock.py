import asyncio
import websockets
import time
import json
responses = []
async def test():

    api_key = "PKDX1ONV8MASSY7TKAAG"
    secret_key = "hvSF9OV0X9IXR6140I6nZcxEgVVOMaQKQoq7hWBo"
    # next_command = """{"action":"subscribe","trades":["BTC/USD"],"quotes":["LTC/USD","ETH/USD"],"bars":["BCH/USD"]}"""
    next_command = """{"action":"subscribe","trades":["BTC/USD"],"bars":["BCH/USD"]}"""
    async with websockets.connect('wss://stream.data.alpaca.markets/v1beta3/crypto/us') as websocket:
        response = await websocket.recv()
        print(response)
        await websocket.send("""{"action": "auth", "key": "PKDX1ONV8MASSY7TKAAG", "secret": "hvSF9OV0X9IXR6140I6nZcxEgVVOMaQKQoq7hWBo"}""")
        response = await websocket.recv()
        print(response)
        await websocket.send(next_command)
        response = await websocket.recv()
        print(response)
        start_time = time.time()
        while time.time() - start_time <40:
            response = await websocket.recv()
            responses.append(response)
            print(response)
        # time.sleep(30)

asyncio.get_event_loop().run_until_complete(test())

for i in responses:
    i_ = json.loads(i.replace("'", '"'))
    print(i_)
    print(type(i_))
