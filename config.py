# Your TechZ Api Key
# Get from @TechZApiBot on Telegram | https://t.me/TechZApiBot

from os import getenv


API_KEY = "api.anime-dex.workers.dev"

if not API_KEY or API_KEY == "api.anime-dex.workers.dev" or API_KEY == "":
    API_KEY = getenv("API_KEY")

    if not API_KEY:
        raise Exception("Please add your TechZ Api Key in config.py file")
