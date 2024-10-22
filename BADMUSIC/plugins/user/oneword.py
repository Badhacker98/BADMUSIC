import random
import time
from pyrogram.types import Message
from random import choice
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram import filters, Client

# import 
from BADMUSIC.misc import SUDOERS as SUDO_USER
from BADMUSIC.cplugin.utils.data import RAID, PBIRAID, OneWord, HIRAID, PORM, EMOJI, GROUP, VERIFIED_USERS



@Client.on_message(filters.command("oneword", prefixes=".") & SUDO_USER)
async def raid(Client: Client, m: Message):  
      Bad = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Bad) == 2:
        counts = int(Bad[0])
        username = Bad[1]
        if not counts:
          await m.reply_text(f"ONEWORDRAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
          return       
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await Client.get_users(Bad[1])
        except:
           await m.reply_text("**Error:** User not found or may be deleted!")
           return
      elif m.reply_to_message:
        counts = int(Bad[0])
        try:
           user = await Client.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("Usage: .oneraid count username or reply")
        return
      if int(m.chat.id) in GROUP:
         await m.reply_text("**Sorry !! i Can't Spam Here.**")
         return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("I can't oneraid on my developer")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("This guy is a sudo users.")
         return
      mention = user.mention
      for _ in range(counts): 
         r = f"{mention} {choice(OneWord)}"
         await Client.send_message(m.chat.id, r)
         await asyncio.sleep(0.3)
