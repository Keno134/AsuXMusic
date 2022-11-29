from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "12410871"))
API_HASH = getenv("API_HASH", "f7a7de22f129870e74bd87e9ef5320bd")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5418087889:AAFwuUGyhN0jOQPkLKYo308AjgrB80WTmOY")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001891060939"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Daddy99:Daddy99@cluster0.czzmfwl.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5399623240").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/184accb94eee032152a03.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f6107be777a5125f07539.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AnimeChatMystic")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MysticXnetwork")

STRING_SESSION = getenv("STRING_SESSION", "BQBVJ8cvnSJCQNwzXjB_781qRGA-8FwfnnlTlwn54ds8kYdgfjA3kGpUBLOHlTIPq7p3nlZYSSZFFPyJrdB74r7wCHxYiYhi6-L2PdyRjfg8C2dfbqZSq6DwjdN1l5x9XEumKBkZH5nzUKrhJ3cQ3gOaor65VeLDFZ6_FMSzjL8C_bhrx70cPsY4S-czWlZl-Mt-JNzKyi-_0dxQwqyDmKxCRKh63YL6F7wxvxfrZ6oFBhxaZKbjw-4sDYXgYa9e6R-JY_lqdAFEaujlsF5LPa-Eww711DCkV9oRD1cSEDm66fEfNpyorWgoPDlOw9P33Nce3xq2UeNZmdYr_fgNZ56DAAAAAVRpAwcA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5732788031").split()))
