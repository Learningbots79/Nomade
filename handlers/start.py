# ============================================================
#Group Manager Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================


from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATE_CHANNEL, START_IMAGE, OWNER_ID
import db

def register_handlers(app: Client):

# ==========================================================
# Start Message
# ==========================================================
    async def send_start_menu(message, user):
        text = f"""

❍ нєу {user} ! 💕
❍ ᴛʜɪs ɪs ⋆⏤‌‌‌‌ 𝙂𝙍𝙊𝙐𝙋 𝙃𝙀𝙇𝙋
╔══════════════════╗
     📝 𝗛𝗜𝗚𝗛𝗟𝗜𝗚𝗛𝗧𝗦 📌
╚══════════════════╝
❍ sᴍᴀʀᴛ ᴀɴᴛɪ-sᴘᴀᴍ & ʟɪɴᴋ sʜɪᴇʟᴅ
❍ ᴀᴅᴀᴘᴛɪᴠᴇ ʟᴏᴄᴋ sʏsᴛᴇᴍ (ᴜʀʟ's, ᴍᴇᴅɪᴀ, ʟᴀɴɢᴜᴀɢᴇ & ᴍᴏʀᴇ)
❍ ᴍᴏᴅᴜʟᴀʀ & sᴄᴀʟᴀʙʟᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ
❍ sʟᴇᴇᴋ ᴜɪ ᴡɪᴛʜ ɪɴʟɪɴᴇ ᴄᴏɴᴛʀᴏʟs

» ᴍᴏʀᴇ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs ᴄᴏᴍɪɴɢ sᴏᴏɴ ...
"""

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("˹ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ˼", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [
                InlineKeyboardButton("˹sᴜᴘᴘᴏʀᴛ˼", url=SUPPORT_GROUP),
                InlineKeyboardButton("˹ᴜᴘᴅᴀᴛᴇ˼", url=UPDATE_CHANNEL),
            ],
            [
                InlineKeyboardButton("˹ᴏᴡɴᴇʀ˼", url=f"tg://openmessage?user_id={OWNER_ID}"),
                InlineKeyboardButton("˹ɢʀᴏᴜᴘ˼", url="https://t.me/+vtycyXXk3UE0NThl"),
                
            ],
            [InlineKeyboardButton("˹ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅ˼", callback_data="help")]
        ])

        # If /start command, send a new photo
        if message.text:
            await message.reply_photo(START_IMAGE, caption=text, reply_markup=buttons)
        else:
            # If callback, edit the same message
            media = InputMediaPhoto(media=START_IMAGE, caption=text)
            await message.edit_media(media=media, reply_markup=buttons)

# ==========================================================
# Start Command
# ==========================================================
    @app.on_message(filters.private & filters.command("start"))
    async def start_command(client, message):
        user = message.from_user
        await db.add_user(user.id, user.first_name)
        await send_start_menu(message, user.first_name)

# ==========================================================
# Help Menu Message
# ==========================================================
    async def send_help_menu(message):
        text = """
╔══════════════════╗
    🆘 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨
╚══════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━
🧑‍💻 ᴄʜᴏᴏsᴇ ᴀ ᴄᴀᴛᴇɢᴏʀʏ ʙᴇʟᴏᴡ ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴄᴏᴍᴍᴀɴᴅs:
━━━━━━━━━━━━━━━━━━━━━━━━
"""
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("˹ɢʀᴇᴇᴛɪɴɢs˼", callback_data="greetings"),
                InlineKeyboardButton("˹ʟᴏᴄᴋs˼", callback_data="locks"),
            ],
            [
                InlineKeyboardButton("˹ᴍᴏᴅᴇʀᴀᴛɪᴏɴ˼", callback_data="moderation")
            ],
            [InlineKeyboardButton("🔙 ˹ʙᴀᴄᴋ˼", callback_data="back_to_start")]
        ])

        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await message.edit_media(media=media, reply_markup=buttons)

# ==========================================================
# Help Callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("help"))
    async def help_callback(client, callback_query):
        await send_help_menu(callback_query.message)
        await callback_query.answer()

# ==========================================================
# back to start Callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("back_to_start"))
    async def back_to_start_callback(client, callback_query):
        user = callback_query.from_user.first_name
        await send_start_menu(callback_query.message, user)
        await callback_query.answer()

# ==========================================================
# Greetings Callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("greetings"))
    async def greetings_callback(client, callback_query):
        text = """
╔══════════════════╗
  ⚙️ 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗦𝗬𝗦𝗧𝗘𝗠
╚══════════════════╝

🎚️ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴍᴀɴᴀɢᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs:

¤ /setwelcome : sᴇᴛ ᴀ ᴄᴜsᴛᴏᴍ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ
¤ /welcome on : ᴇɴᴀʙʟᴇ ᴛʜᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs
¤ /welcome off : ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs

🎛️ sᴜᴘᴘᴏʀᴛᴇᴅ ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs:

¤ {ᴜsᴇʀɴᴀᴍᴇ} : ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀɴᴀᴍᴇ
¤ {ғɪʀsᴛ_ɴᴀᴍᴇ} : ᴜsᴇʀ's ғɪʀsᴛ ɴᴀᴍᴇ
¤ {ɪᴅ} : ᴜsᴇʀ ɪᴅ
¤ {ᴍᴇɴᴛɪᴏɴ} : ᴍᴇɴᴛɪᴏɴ ᴜsᴇʀ ɪɴ ᴍᴇssᴀɢᴇ

🧾 ᴇxᴀᴍᴘʟᴇ:
¤ /sᴇᴛᴡᴇʟᴄᴏᴍᴇ ʜᴇʟʟᴏ {ғɪʀsᴛ_ɴᴀᴍᴇ}! ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {ᴛɪᴛʟᴇ}!
"""
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="help")]
        ])
        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await callback_query.message.edit_media(media=media, reply_markup=buttons)
        await callback_query.answer()

# ==========================================================
# Locks callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("locks"))
    async def locks_callback(client, callback_query):
        text = """
╔══════════════════╗  
   🔐 𝗟𝗢𝗖𝗞 𝗦𝗬𝗦𝗧𝗘𝗠  
╚══════════════════╝  
  
🔏ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴍᴀɴᴀɢᴇ ʟᴏᴄᴋs:  
  
¤ /lock    : ᴇɴᴀʙʟᴇ ᴀ ʟᴏᴄᴋ ғᴏʀ ᴛʜᴇ ɢʀᴏᴜᴘ  
¤ /unlock : ᴅɪsᴀʙʟᴇ ᴀ ʟᴏᴄᴋ ғᴏʀ ᴛʜᴇ ɢʀᴏᴜᴘ  
¤ /locks    : sʜᴏᴡ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ʟᴏᴄᴋs  
  
🔒ᴀᴠᴀɪʟᴀʙʟᴇ ʟᴏᴄᴋ ᴛʏᴘᴇs:  
¤ ᴜʀʟ        : ʙʟᴏᴄᴋ ʟɪɴᴋs  
¤ sᴛɪᴄᴋᴇʀ : ʙʟᴏᴄᴋ sᴛɪᴄᴋᴇʀs  
¤ ᴍᴇᴅɪᴀ    : ʙʟᴏᴄᴋ ᴘʜᴏᴛᴏs / ᴠɪᴅᴇᴏs / ɢɪғs  
¤ ᴜsᴇʀɴᴀᴍᴇ  : ʙʟᴏᴄᴋ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ @ᴜsᴇʀɴᴀᴍᴇ ᴍᴇɴᴛɪᴏɴs  
¤ ʟᴀɴɢᴜᴀɢᴇ  : ʙʟᴏᴄᴋ ɴᴏɴ-ᴇɴɢʟɪsʜ ᴍᴇssᴀɢᴇs  
  
🔓ᴇxᴀᴍᴘʟᴇ:  
¤ /lock url       : ʙʟᴏᴄᴋs ᴀɴʏ ᴍᴇssᴀɢᴇs ᴄᴏɴᴛᴀɪɴɪɴɢ ʟɪɴᴋs  
 ¤ /unlock sticker : ᴀʟʟᴏᴡs sᴛɪᴄᴋᴇʀs ᴀɢᴀɪɴ
"""
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 ˹ʙᴀᴄᴋ˼", callback_data="help")]
        ])
        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await callback_query.message.edit_media(media=media, reply_markup=buttons)
        await callback_query.answer()

# ==========================================================
# Moderation Callback_query
# ==========================================================
    @app.on_callback_query(filters.regex("moderation"))
    async def info_callback(client, callback_query):
        try:
            text = """
╔══════════════════╗
 🧑‍💻𝗠𝗢𝗗𝗘𝗥𝗔𝗧𝗜𝗢𝗡 𝗦𝗬𝗦𝗧𝗘𝗠
╚══════════════════╝

🧑‍💻ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴇᴀsɪʟʏ ᴡɪᴛʜ ᴛʜᴇsᴇ ᴛᴏᴏʟs:

¤ /kick  — ʀᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ  
¤ /ban  — ʙᴀɴ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ  
¤ /unban  — ʟɪғᴛ ʙᴀɴ  
¤ /mute  — ᴅɪsᴀʙʟᴇ ᴍᴇssᴀɢᴇs  
¤ /unmute  — ᴀʟʟᴏᴡ ᴍᴇssᴀɢᴇs ᴀɢᴀɪɴ  
¤ /warn  — ᴀᴅᴅ ᴡᴀʀɴɪɴɢ (3 = ᴍᴜᴛᴇ)  
¤ /warns  — ᴠɪᴇᴡ ᴡᴀʀɴɪɴɢs  
¤ /resetwarns  — ᴄʟᴇᴀʀ ᴀʟʟ ᴡᴀʀɴɪɴɢs  
¤ /promote  — ᴍᴀᴋᴇ ᴀᴅᴍɪɴ  
¤ /demote  — ʀᴇᴍᴏᴠᴇ ғʀᴏᴍ ᴀᴅᴍɪɴ  

💡 ᴇxᴀᴍᴘʟᴇ:
ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ᴛʏᴘᴇ  
/ban @username
"""
            buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 ˹ʙᴀᴄᴋ˼", callback_data="help")]
            ])
    
            media = InputMediaPhoto(media=START_IMAGE, caption=text)
            await callback_query.message.edit_media(media=media, reply_markup=buttons)
            await callback_query.answer()
    
        except Exception as e:
            print(f"Error in info_callback: {e}")
            await callback_query.answer("❌ Something went wrong.", show_alert=True)
    

# ==========================================================
# Broadcast Command
# ==========================================================
    @app.on_message(filters.private & filters.command("broadcast"))
    async def broadcast_message(client, message):
        if not message.reply_to_message:
            await message.reply_text("⚠️ Please reply to a message to broadcast it.")
            return

        if message.from_user.id != OWNER_ID:
            await message.reply_text("❌ Only the bot owner can use this command.")
            return

        text_to_send = message.reply_to_message.text or message.reply_to_message.caption
        if not text_to_send:
            await message.reply_text("⚠️ The replied message has no text to send.")
            return

        users = await db.get_all_users()
        sent, failed = 0, 0

        await message.reply_text(f"Broadcasting to {len(users)} users..")

        for user_id in users:
            try:
                await client.send_message(user_id, text_to_send)
                sent += 1
            except Exception:
                failed += 1

        await message.reply_text(f"✅ Broadcast finished!\n\n Sent: {sent}\nFailed: {failed}")

# ==========================================================
# stats Command
# ==========================================================
    @app.on_message(filters.private & filters.command("stats"))
    async def stats_command(client, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply_text("❌ Only the bot owner can use this command")

        users = await db.get_all_users()
        return await message.reply_text(f"💡 Total users: {len(users)}")
