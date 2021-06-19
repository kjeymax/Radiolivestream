
from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from utils.vc import mp, RADIO
from config import Config
STREAM_URL=Config.STREAM_URL
ADMINS=Config.ADMINS

@Client.on_message(filters.command("radio") & filters.user(ADMINS))
async def radio(client, message: Message):
    if 1 in RADIO:
        await message.reply_text(f"{emoji.ROBOT} **Please Stop Existing Radio Stream By /stopradio Command!**")
        return
    await mp.start_radio()
    await message.reply_text(f"{emoji.CHECK_MARK_BUTTON} **Radio Stream Started :** \n<code>{STREAM_URL}</code>")

@Client.on_message(filters.command("stopradio") & filters.user(ADMINS))
async def stop(_, message: Message):
    if 0 in RADIO:
        await message.reply_text(f"{emoji.ROBOT} **Please Start A Radio Stream First By /radio Command!**")
        return
    await mp.stop_radio()
    await message.reply_text(f"{emoji.CROSS_MARK_BUTTON} **Radio Stream Ended Successfully!**")
