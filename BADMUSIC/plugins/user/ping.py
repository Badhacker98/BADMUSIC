import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from platform import python_version
from BADMUSIC.misc import SUDOERS as SUDO_USER
from config import*

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command("alive", prefixes=".") & SUDO_USER)
async def alive(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    txt = (
        f" ⌬ **ᴍᴜsɪᴄ ☆ ᴜsᴇʀʙᴏᴛ ☆ ᴀʟɪᴠᴇ** ⌬︎︎\n\n"
        f"⌬ ᴠᴇʀsɪᴏɴ ➪︎ 2.0\n"
        f"⌬ ᴘɪɴɢ ➪ {ping * 1000:.3f}ᴍs\n"
        f"⌬ ᴜᴘ ☆ ᴛɪᴍᴇ ➪︎ {uptime}\n"
        f"⌬ ᴘʏᴛʜᴏɴ ➪︎ {python_version()}`\n"
        f"⌬ ᴘʏʀᴏɢʀᴀɴ ➪︎ {__version__}\n"
        f"⌬ ᴏᴡɴᴇʀ ➪︎ {client.me.mention}"    
    )
    await message.delete()
    await message.reply_photo(photo=UC_IMG_URL, caption=txt)

@Client.on_message(filters.command("ping", prefixes=".") & SUDO_USER)
async def ping(client: Client, message: Message):
    r = await message.reply_text("**ᴘᴏɴɢ**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"⌬ **ᴍᴜsɪᴄ ᴜsᴇʀʙᴏᴛ** ⌬\n\n"
        f"⌬ ᴘɪɴɢ ➪ {ping * 1000:.3f}ᴍs\n"
        f"⌬ ᴜᴘ ☆ ᴛɪᴍᴇ ➪ {uptime}\n"
        f"⌬ ᴏᴡɴᴇʀ ➪{client.me.mention}\n"
    )
    await message.delete()
    await message.reply_photo(photo=UC_IMG_URL, caption=txt)

