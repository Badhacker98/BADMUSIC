import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from platform import python_version
from BADMUSIC.misc import SUDOERS as SUDO_USER

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


@Client.on_message(filters.command("ping", prefixes=".") & SUDO_USER)
async def ping(client: Client, message: Message):
    r = await message.reply_text("**🇵𝐎𝐍𝐆**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"★🇦★🇱𝐄★🇨𝐇𝐀𝐊★🇲𝐀𝐈𝐍★🇦★🇬𝐈𝐀 ★\n\n"
        f"🇵𝐈𝐍𝐆 ❥︎ {ping * 1000:.3f}ᴍs\n"
        f"🇺𝐏★🇹𝐈𝐌𝐄 ❥︎ {uptime}\n"
        f"🇴𝐖𝐍𝐄𝐑 ❥︎ {client.me.mention}\n"
        f"🇺𝐒𝐓𝐀𝐃★🇯𝐈 ❥︎ [⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸](@II_BAD_MUNDA_II)"
    )
