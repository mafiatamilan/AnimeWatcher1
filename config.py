# Your TechZ Api Key
# Get from @TechZApiBot on Telegram | https://t.me/TechZApiBot

from os import getenv


API_KEY = "38:5rHubT-s]DNCd#S_^+C!6$n3%r:qM"

if not API_KEY or API_KEY == "38:5rHubT-s]DNCd#S_^+C!6$n3%r:qM" or API_KEY == "":
    API_KEY = getenv("API_KEY")

    if not API_KEY:
        raise Exception("Please add your TechZ Api Key in config.py file")
