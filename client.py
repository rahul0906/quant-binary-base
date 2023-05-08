import asyncio
import websockets
import time
import json

data_queue = asyncio.Queue()
async def test(responses = []):

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
        # x = time.time() - start_time <20
        while True:
            response = await websocket.recv()
            responses.append(response)
            print(response)
            await data_queue.put(response)

async def process_data():
    n=0
    while True:
        data = await data_queue.get()
        print("The data to be processed: ", data)
        n += 1
        print(n)
    # data_queue.task_done()

async def main():
    await asyncio.gather(test(), process_data())


asyncio.get_event_loop().run_until_complete(main())


# responses = asyncio.get_event_loop().run_until_complete(test())
# print(responses)
# responses = test()
# for i in responses:
#     i_ = json.loads(i.replace("'", '"'))
#     print(i_)
#     print(type(i_))
