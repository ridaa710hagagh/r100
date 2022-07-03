import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "11440071"))
    API_HASH = os.environ.get("API_HASH", "f9803f0cdb5630506725e3d5c1b54215")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5157459732:AAH-5tsHQif9_pqUIwnM-wNqRl6NXH39IHk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AgB8NOjtBk_spb_GJeusKqLXS9_vX41mhKWT7ChQfa6gJhTx6NAak6YnOECjCPuj_DhKnIuBRb2xCbeIQMbAO7_v9_zfxbivcznYDIwJPHz6UaJIA7R9kk1D1IIZ36UlkHKD4E6ZFAZU1NmjgyBA80JPn5wFDRZJOCqC2AlC5Lr3ADh6EEM7taVZxlRCsCKzVQJnIUkHcN-F7ouQsC_yD5ALjbha2k1we_KAIQOYoIxs0Khc03gUObgpqtSXaGJuVUZ9zn1h4dQ3XR-voKvhPnudiDJku-EVFRyD9F8_BNUlK53BInnrdWWY355ILtPXqQV0Yd_LrsuABggEbYD8ejf6AAAAATHGe-oA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Dajjla_bot")
    SUPPORT = os.environ.get("SUPPORT", "JMTHON_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "x02x2")
    START_IMG = os.environ.get("START_IMG", "https://l.top4top.io/p_2363dcjiw1.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
