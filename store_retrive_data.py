import requests

from GameTypes import UserData
from constants import BASE_URL_BACK_END
from utils import user_updater


def get_user_data(user_id: int) -> UserData:
    resp = requests.get(BASE_URL_BACK_END + "/api/store/{}".format(user_id))
    data = resp.json()
    user_data = user_updater(UserData(
        user_id=data['user_id'],
        energy=data['energy'],
        balance=data['balance'],
        total_amount=data['total_amount'],
        total_clicks=data['total_clicks'],
        last_clicks=data['last_clicks'],
        limit_level=data['limit_level'],
        speed_level=data['speed_level'],
        multi_tap_level=data['multi_tap_level'],
        auto_bot=data['auto_bot'],
        guru_used=data['guru_used'],
        refill_used=data['refill_used'],
        claimed_tasks=data['claimed_tasks'],
        claimed_leagues=data['claimed_leagues'],
        claimed_ref=data['claimed_ref'],
        referrals=data['referral'],
        # todo: implement last update for this method
        last_update=0
    ))
    return user_data