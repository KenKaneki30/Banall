import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN","7304576231:AAHb5dJRurhOGQmqcMhJ497naZ_qXpsg8xg")
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH= getenv('b30d5a8312842f59f0eb56b147b2702f')
    TELEGRAM_APP_ID=int(getenv('29074416'))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
