import requests

from GameTypes import UserData, SpecialTask
import time

from constants import LEAGUES, BASE_URL_BACK_END


def user_updater(usr: UserData) -> UserData:
    # calculating the tap-bot activation for at most 12 hrs from last update
    time_to_fill_energy = int(((usr['limit_level'] * 500) - usr['energy']) / usr['speed_level']) + 1
    time_elapsed = int(time.time() - usr['last_update'])
    # energy Calculation
    if time_elapsed > time_to_fill_energy:
        usr['energy'] = usr["limit_level"] * 500
    else:
        usr['energy'] += time_elapsed * usr['speed_level']

    # final energy_overflow_check
    if usr['energy'] > usr["limit_level"] * 500:
        usr['energy'] = usr["limit_level"] * 500

    # auto bot calculation
    if usr['auto_bot']:
        time_to_calculate = max(min(43200, time_elapsed - time_to_fill_energy), 0)
        usr['tap_bot_earning'] = time_to_calculate * usr['speed_level']
        usr['balance'] += usr['tap_bot_earning']
    else:
        usr['tap_bot_earning'] = 0


    # calculating special boosts update
    if int(usr['last_update'] / 86400) < int(time.time() / 86400):
        usr["guru_used"] = 0
        usr["refill_used"] = 0

    return usr


def get_tasks():
    response = requests.get(BASE_URL_BACK_END + "/api/manager/tasks")
    tasks = []
    for item in response.json():
        tasks.append(
            SpecialTask(title=item['title'], description=item['title'], url=item['url'], reward=item['amount']))
    return tasks


def get_task_fake():
    tasks = [SpecialTask(title="task title",description="task desc",url=BASE_URL_BACK_END,reward=10023241)]
    return tasks


def league_finder(amount: int):
    current_league = 0
    for item in LEAGUES:
        if amount > item['threshold']:
            current_league += 1
        else:
            break
    return current_league