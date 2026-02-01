# ============================================================
# Group Manager Bot
# Author: learningbots79 (https://github.com/learningbots79)
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

import os
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_all_handlers
from db import db

#  LOGGING 
logging.basicConfig(level=logging.INFO)

#  WEB SERVER (RENDER FIX) 
PORT = int(os.environ.get("PORT", 10000))

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Nomade Help Bot is running")

def start_web_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    logging.info(f"Web server running on port {PORT}")
    server.serve_forever()

threading.Thread(target=start_web_server, daemon=True).start()

#  TELEGRAM BOT 
app = Client(
    "group_manager_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_all_handlers(app)

print("Bot is starting...")

app.run()
