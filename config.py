from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","21944949"))
API_HASH = getenv("API_HASH","d1abedd1624be80538e5d6da730f7963")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID","2107529793"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/957b6c210e5047dd96e55.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/957b6c210e5047dd96e55.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+4oluZavNok1hN2E1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/villain_feelings")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2107529793").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
