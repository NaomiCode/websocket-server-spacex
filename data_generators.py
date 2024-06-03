from GameTypes import UserData, TapPageData, UpgradePageData, TaskPageData
from constants import REF_TASKS, LEAGUES, MULTI_TAP_UPGRADE_PRICE, ENERGY_SPEED_UPGRADE_PRICE, \
    ENERGY_LIMIT_UPGRADE_PRICE, AUTO_BOT_PRICE
from utils import get_tasks, league_finder, get_task_fake


def tap_data_generator(usr: UserData) -> TapPageData:
    return TapPageData(
        multi_tap_level=usr["multi_tap_level"],
        auto_bot=usr["auto_bot"],
        speed_level=usr['speed_level'],
        limit_level=usr['limit_level'],
        max_energy_value=usr['limit_level'] * 500,
        balance=usr['balance'],
        energy=usr['energy'],
        current_league=league_finder(usr['total_amount']),
        auto_bot_earning=usr['tap_bot_earning'])


def upgrade_data_generator(usr: UserData) -> UpgradePageData:
    limit_max = len(ENERGY_LIMIT_UPGRADE_PRICE) == usr['limit_level']
    speed_max = len(ENERGY_SPEED_UPGRADE_PRICE) == usr['speed_level']
    multi_tap_max = len(MULTI_TAP_UPGRADE_PRICE) == usr['multi_tap_level']
    auto_bot_max = usr['auto_bot']

    limit_price = 0
    if not limit_max:
        limit_price = ENERGY_LIMIT_UPGRADE_PRICE[usr['limit_level'] + 1]

    speed_price = 0
    if not speed_max:
        speed_price = ENERGY_SPEED_UPGRADE_PRICE[usr['speed_level'] + 1]

    multi_tap_price = 0
    if not multi_tap_max:
        multi_tap_price = MULTI_TAP_UPGRADE_PRICE[usr['multi_tap_level'] + 1]

    auto_bot_price = 0
    if not auto_bot_max:
        auto_bot_price = AUTO_BOT_PRICE
    return UpgradePageData(
        auto_bot=usr['auto_bot'],
        balance=usr['balance'],
        speed_level=usr['speed_level'],
        limit_level=usr['limit_level'],
        multi_tap_level=usr['multi_tap_level'],
        guru_used=usr['guru_used'],
        refill_used=usr['refill_used'],
        limit_upgrade_price=limit_price,
        speed_upgrade_price=speed_price,
        multi_tap_upgrade_price=multi_tap_price,
        speed_is_max=speed_max,
        limit_is_max=limit_max,
        multi_tap_is_max=multi_tap_max,
        auto_bot_is_max=auto_bot_max,
        auto_bot_upgrade_price=auto_bot_price
    )


def task_data_generator(user: UserData) -> TaskPageData:
    return TaskPageData(
        special_tasks=get_task_fake(),
        special_claimed=user['claimed_tasks'],
        #todo: status task
        ref_tasks=REF_TASKS,
        ref_claimed=user['claimed_ref'],
        league_tasks=LEAGUES,
        league_claimed=user['claimed_leagues'],
        current_ref=len(user['referrals']),
        current_league=league_finder(user['total_amount'])
    )

