import asyncio

from pyrogram import filters
from pyrogram import filters, Client
from pyrogram.types import Message
from BADMUSIC.misc import SUDOERS

spamTask = {}


async def spam_text(
    client: Client,
    chat_id: int,
    to_spam: str,
    count: int,
    reply_to: int,
    delay: float,
    copy_id: int,
    event: asyncio.Event,
):
    for _ in range(count):
        if event.is_set():
            break

        if copy_id:
            await client.copy_message(
                chat_id, chat_id, copy_id, reply_to_message_id=reply_to
            )
        else:
            await client.send_message(
                chat_id,
                to_spam,
                disable_web_page_preview=True,
                reply_to_message_id=reply_to,
            )
        if delay:
            await asyncio.sleep(delay)

    try:
        event.set()
        task = spamTask.get(chat_id, None)
        if task:
            task.remove(event)
    except:
        pass

    await Client.check_and_log(
        "spam",
        f"**Count:** `{count}`\n**Chat:** `{chat_id}`\n**Client:** {client.me.first_name}",
    )


@Client.on_message(filters.command("spam", prefixes=".") & SUDOERS)
async def spamMessage(client: Client, message: Message):
    if len(message.command) < 3:
        return await Client.delete(message, "Give me something to spam.")

    reply_to = message.reply_to_message.id if message.reply_to_message else None
    try:
        count = int(message.command[1])
    except ValueError:
        return await Client.delete(message, "Give me a valid number to spam.")

    to_spam = message.text.split(" ", 2)[2].strip()
    event = asyncio.Event()
    task = asyncio.create_task(
        spam_text(client, message.chat.id, to_spam, count, reply_to, None, None, event)
    )

    if spamTask.get(message.chat.id, None):
        spamTask[message.chat.id].append(event)
    else:
        spamTask[message.chat.id] = [event]

    await message.delete()
    await task


@Client.on_message(filters.command("dspam", prefixes=".") & SUDOERS)
async def delaySpam(client: Client, message: Message):
    if len(message.command) < 4:
        return await Client.delete(message, "Give me something to spam.")

    reply_to = message.reply_to_message.id if message.reply_to_message else None
    try:
        count = int(message.command[1])
    except ValueError:
        return await Client.delete(message, "Give me a valid number to spam.")

    try:
        delay = float(message.command[2])
    except ValueError:
        return await Client.delete(message, "Give me a valid delay to spam.")

    to_spam = message.text.split(" ", 3)[3].strip()
    event = asyncio.Event()
    task = asyncio.create_task(
        spam_text(client, message.chat.id, to_spam, count, reply_to, delay, None, event)
    )

    if spamTask.get(message.chat.id, None):
        spamTask[message.chat.id].append(event)
    else:
        spamTask[message.chat.id] = [event]

    await message.delete()
    await task


@Client.on_message(filters.command("mspam", prefixes=".") & SUDOERS)
async def mediaSpam(client: Client, message: Message):
    if not message.reply_to_message:
        return await Client.delete(message, "Reply to a media to spam.")

    if len(message.command) < 2:
        return await Client.delete(message, "Give me a valid number to spam.")

    try:
        count = int(message.command[1])
    except ValueError:
        return await Client.delete(message, "Give me a valid number to spam.")

    copy_id = message.reply_to_message.id
    event = asyncio.Event()
    task = asyncio.create_task(
        spam_text(client, message.chat.id, None, count, None, None, copy_id, event)
    )

    if spamTask.get(message.chat.id, None):
        spamTask[message.chat.id].append(event)
    else:
        spamTask[message.chat.id] = [event]

    await message.delete()
    await task


@Client.on_message(filters.command("stopspam", prefixes=".") & SUDOERS)
async def stopSpam(_, message: Message):
    chat_id = message.chat.id

    if not spamTask.get(chat_id, None):
        return await Client.delete(message, "No spam task running for this chat.")

    for event in spamTask[chat_id]:
        event.set()

    chat_name = message.chat.title or message.chat.first_name
    del spamTask[chat_id]
    await Client.delete(message, f"Spam task stopped for {chat_name}.")

