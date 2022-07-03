import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "11440071"))
    API_HASH = os.environ.get("API_HASH", "f9803f0cdb5630506725e3d5c1b54215")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Dajjla_bot")
    SUPPORT = os.environ.get("SUPPORT", "JMTHON_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "x02x2")
    START_IMG = os.environ.get("START_IMG", "https://l.top4top.io/p_2363dcjiw1.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
