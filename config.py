from os import path, getenv

class config:
    API_ID = int(getenv("API_ID", "15911095"))
    API_HASH = getenv("API_HASH", "391f344a9957ff3c49d82c2cd5e436af")
    BOT_TOKEN = getenv("BOT_TOKEN", "7202204800:AAFpMiUdEc5aC9iHSnvvcRwIA-5M4wtRl-A")
    IP_API =getenv("ACCESS_TOKEN","ab79b5709c900e")
    
con = config()
