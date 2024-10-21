from config import API_ID, API_HASH
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 
from pyrogram import Client, filters


@Client.on_message(filters.command(["clone"], prefixes=["."]))
async def clone(bot: Client, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n .clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
        client = Client(name="BADMUSIC", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="BADMUSIC/plugins/user"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
