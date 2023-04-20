from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","21944949"))
API_HASH = getenv("API_HASH","d1abedd1624be80538e5d6da730f7963")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID","2107529793"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/e68f585a0a2e4e5dc1164.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/e68f585a0a2e4e5dc1164.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LOVE_FEELINGS_WILL1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LOVE_FEELINGS_WILL")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2107529793").split()))


FAILED = "https://te.legra.ph/file/e68f585a0a2e4e5dc1164.jpg"
