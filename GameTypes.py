from typing import TypedDict
from typing_extensions import NotRequired


class RefTask(TypedDict):
    title: str
    reward: int
    threshold: int


class LeagueType(TypedDict):
    title: str
    reward: int
    threshold: int


class UserData(TypedDict):
    user_id: int
    energy: int
    balance: int
    total_amount: int
    total_clicks: int
    last_clicks: int
    limit_level: int
    speed_level: int
    multi_tap_level: int
    auto_bot: bool
    guru_used: int
    refill_used: int
    claimed_tasks: list[int]
    claimed_leagues: list[int]
    claimed_ref: list[int]
    referrals: list[int]
    last_update: int
    tap_bot_earning: NotRequired[int]


class TapPageData(TypedDict):
    balance: int
    current_league: int
    energy: int
    limit_level: int  # *500 must be applied
    max_energy_value: int
    speed_level: int
    multi_tap_level: int
    auto_bot: bool
    auto_bot_earning: int


class UpgradePageData(TypedDict):
    balance: int
    limit_level: int
    limit_upgrade_price: int
    limit_is_max: bool
    speed_level: int
    speed_upgrade_price: int
    speed_is_max: bool
    multi_tap_level: int
    multi_tap_upgrade_price: int
    multi_tap_is_max: bool
    auto_bot: bool
    auto_bot_upgrade_price: int
    auto_bot_is_max: bool
    guru_used: int
    refill_used: int


class SpecialTask(TypedDict):
    title: str
    description: str
    url: str
    reward: int


class TaskPageData(TypedDict):
    special_tasks: list[SpecialTask]
    special_claimed: list[int]
    ref_tasks: list[RefTask]
    ref_claimed: list[int]
    league_tasks: list[dict]
    league_claimed: list[int]
    current_ref: int
    current_league: int
