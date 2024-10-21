import asyncio
import random
import time
from pyrogram.types import Message
from random import choice
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram import filters, Client
from BADMUSIC.cplugin.utils.data import RAID, PBIRAID, OneWord, HIRAID, PORM, EMOJI


@Client.on_message(filters.command("raid", prefixes=".") & SUDOERS)
async def raid(x: Client, e: Message):
      PbxTeam = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(PbxTeam) == 2:
          ok = await x.get_users(kex[1])
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(RAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(RAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("Rᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  

#pbiraid

@Client.on_message(filters.command("pbiraid", prefixes=".") & SUDOERS)
async def raid(x: Client, e: Message):
      PbxTeam = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(PbxTeam) == 2:
          ok = await x.get_users(kex[1])
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(PBIRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(PBIRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("ᴘʙɪʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  


#oneword

@Client.on_message(filters.command("oneword", prefixes=".") & SUDOERS)
async def raid(x: Client, e: Message):
      PbxTeam = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(PbxTeam) == 2:
          ok = await x.get_users(kex[1])
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(OneWord)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(OneWord)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("ᴏɴᴇᴡᴏʀᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  


#HIRAID

@Client.on_message(filters.command("hiraid", prefixes=".") & SUDOERS)
async def raid(x: Client, e: Message):
      PbxTeam = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(PbxTeam) == 2:
          ok = await x.get_users(kex[1])
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(HIRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(HIRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("ʜɪʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  


#porn
@Client.on_message(filters.command("pornspam", prefixes=".") & SUDOERS)
async def prns(client: Client, message: Message):
    r = await message.reply_text("`ʀᴜᴋᴏ ʙʙʏs🤤🫧`")
    quantity = message.command[1]
    failed = 0
    quantity = int(quantity)
    await r.delete()
    if int(message.chat.id) in GROUP:
        await message.reply_text("`ʏᴏᴜ ᴄᴀɴɴᴏᴛ ᴘᴏʀɴꜱᴘᴀᴍ ɪɴ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴄʜᴀᴛꜱ!`")
        return
    for _ in range(quantity):
        try:
            file = random.choice(PORM)            
            await client.send_video(chat_id=message.chat.id, video=file)
        except FloodWait as e:
            await asyncio.sleep(e.x)


#eomji

@Client.on_message(filters.command("emojii", prefixes=".") & SUDOERS)
async def emoji(x: Client, e: Message):
      PBX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(PBX) == 2:
          ok = await x.get_users(PBX[1])
          counts = int(PBX[0])
          for _ in range(counts):
                reply = choice(EMOJI)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(PBX[0])
          for _ in range(counts):
                reply = choice(EMOJI)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text(".emoji 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")
            
