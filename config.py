import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 6888478102

MSG_EFFECT = 5046509860389126442

SHORT_URL = "linkshortify.com" # shortner url 
SHORT_API = "7a541402aeacbdbff361696add89bce2cf8afa4e" 
SHORT_TUT = "https://t.me/How_to_Download_otx"

# Bot Configuration
SESSION = "diablo"
TOKEN = "8477674355:AAF79F7jiobR6B4lV79gwvHcDGfd6jWEMuM"
API_ID = "26944587"
API_HASH = "7261a455f2a6159b8a2fbfecd1a63004"
WORKERS = 5

DB_URI = "mongodb"
DB_NAME = "yato"

FSUBS = [[-1002490852825, True, 10] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = [-1003483464561]   # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [7252834931, 7813956229, 5879656694]
# Bot Settings
DISABLE_BTN = True
PROTECT = True

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>ᴀɴɪᴍᴇ ʟᴏᴠᴇʀs? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ aʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: @Anime_Mines \n <blockquote expandable>›› ᴍᴀɴᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/otakumines_network'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› ᴏᴡɴᴇʀ: @Diablovolfir0\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @Diablovolfir0</b></blockquote>",
    "REPLY": "<b>For More Join - @Anime_Mines</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://telegra.ph/file/60c86ee99686ee503edef-0c2f86c8caa715c8ab.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/fdad63f685759861166e1-5b8901f5a0daf04ace.jpg",
    "SHORT_PIC": "https://telegra.ph/file/48788261ae8fe52a75450-6deb25995eaba4230a.jpg",
    "SHORT": "https://telegra.ph/file/60c86ee99686ee503edef-0c2f86c8caa715c8ab.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
