import asyncio
from websockets import WebSocketServerProtocol
from websockets.server import serve


async def ponger(wss: WebSocketServerProtocol):
    await wss.send("pong")


def pong(wss: WebSocketServerProtocol):
    print("pong")
    loop = asyncio.new_event_loop()
    loop.run_until_complete(ponger(wss))


async def handler(websocket: WebSocketServerProtocol):
    user_id = websocket.request_headers.get("User-Id")

    async for message in websocket:
        if message == "ping":
            await websocket.send("pong")
            print("pppp")

            async def periodic():
                while True:
                    print('periodic')
                    await websocket.send("period")
                    await asyncio.sleep(1)  # you can put 900 seconds = 15mins

            def stop():
                task.cancel()

            loop = asyncio.get_event_loop()
            loop.call_later(500, stop)  # increase end time as per your requirement
            task = loop.create_task(periodic())
        else:
            await websocket.send("@@@kire khar")
            # try:
            #     loop.run_until_complete(task)
            # except asyncio.CancelledError:
            #     pass
        # if message == "id":
        #     await websocket.send("user_id")
        # elif message == "name":
        #     await websocket.send("username")
        # else:
        #     await websocket.send("kiri")


async def main():
    async with serve(handler, "localhost", 8080):
        await asyncio.Future()  # run forever


asyncio.run(main())
