from GameTypes import RefTask, LeagueType
BASE_URL_BACK_END = "http://192.168.88.167:8002"


REF_TASKS = [
    RefTask(title="invite 1 friends", reward=25_000, threshold=1),
    RefTask(title="invite 3 friends", reward=50_000, threshold=3),
    RefTask(title="invite 10 friends", reward=200_000, threshold=10),
    RefTask(title="invite 25 friends", reward=250_000, threshold=25),
    RefTask(title="invite 50 friends", reward=300_000, threshold=50),
    RefTask(title="invite 100 friends", reward=500_000, threshold=100),
    RefTask(title="invite 500 friends", reward=2_000000, threshold=500),
    RefTask(title="invite 1000 friends", reward=2_500000, threshold=1000),
    RefTask(title="invite 10000 friends", reward=10_000000, threshold=10000),
    RefTask(title="invite 100000 friends", reward=100_000000, threshold=100000),
]

LEAGUES = [
    LeagueType(title="Wooden League", reward=500, threshold=0),
    LeagueType(title="Bronze League", reward=1000, threshold=1),
    LeagueType(title="Silver League", reward=5000, threshold=5000),
    LeagueType(title="Gold League", reward=10000, threshold=50000),
    LeagueType(title="Platinum League", reward=25000, threshold=250000),
]

ENERGY_LIMIT_UPGRADE_PRICE = [200, 500, 1000, 5000, 25000, 100000, 200000]
ENERGY_SPEED_UPGRADE_PRICE = [2000, 10000, 50000, 100000, 250000]
MULTI_TAP_UPGRADE_PRICE = [200, 500, 1000, 2500, 25000, 100000, 200000]
AUTO_BOT_PRICE = 200_000
