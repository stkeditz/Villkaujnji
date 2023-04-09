from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","19212195"))
API_HASH = getenv("API_HASH","96a188e8112f0bbeacae20e10817d1f6")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID","6117249994"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION","BQB2kRkEUE7cp0YE5m-270uQeyYPg9-DMFbvpkE-0q-x4C35hUjIEiPOap1H60TOHgSSwJPQbAGsiI2Zt8eSaxBe25v8aVkT42GQrtTs6BstPlcPHuMOuExM8irlnuXI-CTpIcplVBYtIhwO4uHKPaXWUMPYMllwzpB3G41V9hvCHDnV5m3ZFzD1zsik5GbGowQDDZtEhy2hUxY92Dm40OpsVqY5TKKKXIVYFIaaiTQ5ToTOpOVri1IbNUbhtA1gRHtlz9NpnG-JY7vmh6ELO1BaVcxPce0yokGWTrhlyyX-EH-acTk5fYdbC570fEVfTj-VuQfoH1_PfB_YcsRRaeAAAAAWp7l-4A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SankiDiscuss")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
