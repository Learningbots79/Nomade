# ============================================================
# Group Manager Bot
# Author: learningbots79 (https://github.com/learningbots79) 
# Support: https://t.me/learning_bots
# Channel: https://t.me/learningbots79
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import logging
from handlers import register_all_handlers
from db import db

logging.basicConfig(level=logging.INFO)

app = Client(
    "group_manger_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_all_handlers(app)

print("Bot is starting... ")

app.run()