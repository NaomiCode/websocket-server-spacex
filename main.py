import json
import time

from GameTypes import UserData
from data_generators import tap_data_generator, upgrade_data_generator, task_data_generator
from utils import user_updater
import asyncio
from websockets import WebSocketServerProtocol
from websockets.server import serve


def get_user_data_fake(user_id: int) -> UserData:
    data = UserData(user_id=12, energy=990, balance=253, total_amount=1000, total_clicks=123, last_clicks=1214512343,
                    limit_level=2, speed_level=1, multi_tap_level=2, auto_bot=True, guru_used=0, refill_used=3,
                    claimed_tasks=[], claimed_leagues=[], claimed_ref=[], referrals=[],
                    last_update=int(time.time()) - 100)
    data = user_updater(data)
    return data


async def guru_activation(websocket: WebSocketServerProtocol):
    await websocket.send("guru activated")
    await asyncio.sleep(5)
    await websocket.send("guru deactivated")


async def handler(websocket: WebSocketServerProtocol):
    user_id = websocket.path[1:]
    print(user_id)
    user_data = get_user_data_fake(user_id)
    # await websocket.send(json.dumps(tap_data_generator(user_data)))
    # await websocket.send(tap_ data_generator(user_data).__str__())

    async for message in websocket:
        #todo: guru activate
        #todo: omit limit level;
        print(message)
        if message == "tap data":
            await websocket.send(tap_data_generator(user_data).__str__())
        elif message == "upgrade data":
            # todo: next update guru
            await websocket.send(upgrade_data_generator(user_data).__str__())
        elif message == "task data":
            # todo: claimable add, leagues omit, non claimable, ref list omit
            await websocket.send(task_data_generator(user_data).__str__())
        elif message == "guru":
            loop = asyncio.get_running_loop()
            loop.create_task(guru_activation(websocket))
        elif message == "tap":
            await websocket.send(json.dumps({"topic": "tap", "result": {"status": "success", "tap": "2"}}))


async def main():
    async with serve(handler, "0.0.0.0", 8080):
        print("started at :8080")
        await asyncio.Future()  # run forever


asyncio.run(main())
