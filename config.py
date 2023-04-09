from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","21944949"))
API_HASH = getenv("API_HASH","d1abedd1624be80538e5d6da730f7963")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID","2107529793"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LOVE_FEELINGS_WILL1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LOVE_FEELINGS_WILL1")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
