import time, os
from pyrogram import filters, __version__
from pytgcalls import __version__ as version
from pyrogram import filters, Client
from BADMUSIC.utils.decorators.language import language

# ---------------------------
@Client.on_message(filters.command(["alive"], prefixes=["."]) & ~BANNED_USERS)
@language
def alive(_, message):
    message.reply_text("**🥀 I Aᴍ Aʟɪᴠᴇ Mʏ Dᴇᴀʀ Gᴇɴɪᴜs Mᴀsᴛᴇʀ ✨ @ll_BAD_MUNDA_ll **")
  
