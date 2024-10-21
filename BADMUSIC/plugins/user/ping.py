import time, os
from pyrogram import filters, __version__
from pytgcalls import __version__ as version
from pyrogram import filters, Client
from BADMUSIC.utils.decorators.language import language



ping_txt = """
**ᴘɪɴɢ ᴘᴏɴɢ ⚡**

⌬ **ᴛɪᴍᴇ ᴛᴀᴋᴇʀ** - `{}`ms
⌬ **ᴘʏʀᴏɢʀᴀᴍ** - `{}`
⌬ **ᴘʏᴛɢᴄᴀʟʟs** - `{}`
"""

@Client.on_message(filters.command(["ping"], prefixes=["."]) & ~BANNED_USERS)
@language
async def ping_cmd(client, message):
    start_time = time.time()
    a = await message.reply("ᴍᴜsɪᴄ ᴜsᴇʀʙᴏᴛ...")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000)    
    await a.edit_text(ping_txt.format(ping_time,__version__, version))
