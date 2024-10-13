# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "17833358"))
	API_HASH = os.environ.get("API_HASH","b52cd2b77ec1833ec5b96a9d70a363bb")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "7236258270:AAFlhsx6Z2KVKQjla4NnAx-pvkLepAX4i_E")
	BOT_USERNAME = os.environ.get("BOT_USERNAME","KuttyFileSharing_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002105619071"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5691291380"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Itachi:15@itachiuchicha.3nsc8.mongodb.net/?retryWrites=true&w=majority&appName=ItachiUchicha")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002400430988")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL","-1002272796218")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @AbirHasan2005

👥 **Support Group:** [Linux Repositories](https://t.me/DevsZone)

📢 **Updates Channel:** [Discovery Projects](https://t.me/Discovery_Updates)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @AbirHasan2005

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/AbirHasan2005) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
