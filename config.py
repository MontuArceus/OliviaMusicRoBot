from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("26060023"))
API_HASH = getenv("6db95f722004e89e5916b974bfe1d144")

BOT_TOKEN = getenv("6886342923:AAGfcLURqEJrJlLBQbnx98uUJXKi_iKJb4c", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("BQGNpPcAcE_r5y8vX7KbBEUfutksjj1rSw9LAKpckA4llFby0n4HI7e4JQEwqnzUBhQWwTKKImfO0hQRGnjSO4HH8se_bM2MKy8k5mkdJec1_sacS2WNEf_SNx41LpWZKgeYdUeQ5JWHvFGlekJfXyv4QsvK58E9QMqf68b-LyH_xRX5rUIiwB722vt2HzJoa8THm-tR5gNrG2w6vzRahpB6U8gDT0G0X9RuwwrnZgy0wSmE06-OONyD32d2GvRFCTWXmslOMo1pmAbwoF78bm1S_d9Z8kx73I99RzS6OXx57iHsVFdC26ezzM8UKFi3ys-DFCBvSmpmZ6cpz5znNqilCOnVeQAAAABnp4VhAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/extensa_07")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/extensamusicbot")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1739031905").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
