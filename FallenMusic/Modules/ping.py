import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from FallenMusic import BOT_NAME, StartTime, app
from FallenMusic.Helpers import get_readable_time


@app.on_message(filters.command("ping"))
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} ɪs ᴘɪɴɢɪɴɢ..."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""**» ᴘᴏɴɢ ʙᴀʙʏ «**\n`💘 {0} ᴍs`\n\n<b><u>{1} sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴅɪʟ ᴍᴜsɪᴄ :</u></b>\n\n             🍃 ᴜᴩᴛɪᴍᴇ : {2}\n»»————- ★ - ★ ————-««\n             ❣️ ʀᴀᴍ : {3}\n»»————- ★ - ★ ————-««\n             ❣️ ᴄᴩᴜ : {4}\n»»————- ★ - ★ ————-««\n             ❣️ ᴅɪsᴋ : {5}\n»»————- ★ - ★ ————-««\n             🍃 ᴩʏ-ᴛɢᴄᴀʟʟs : {6}ᴍs\n»»————- ★ - ★ ————-««\n\n **💞🌹ᴀᴀʀᴏʜɪ ɪ ʟᴏᴠᴇ ʏᴏᴜ sᴏ ᴍᴜᴄʜ🌹💞**\n\n ◈ ━━━━━━━ ⸙ - ⸙ ━━━━━━━ ◈\n🍃ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ᴅᴏsᴇɴ'ᴛ ɴᴇᴇᴅ ᴄᴜᴛᴇ ᴠᴏɪᴄᴇ ᴀɴᴅ ʟᴏᴠᴇʟʏ ғᴀᴄᴇ...🥺\n
ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ɴᴇᴇᴅs ᴘᴜʀᴇ ʜᴇᴀʀᴛ ᴡɪᴛʜ ᴜɴʙʀᴇᴀᴋᴀʙʟᴇ ᴛʀᴜsᴛ🥀...🍃\n◈ ━━━━━━━ ⸙ - ⸙ ━━━━━━━ ◈\n\n || ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ [ᴅɪʟ❣️](https://t.me/Honey_Singh_121) 🥀 ||\n\n""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❄ sᴜᴘᴘᴏʀᴛ ❄", url=config.SUPPORT_CHAT),
                    InlineKeyboardButton(
                        "✨ sᴏᴜʀᴄᴇ ✨",
                        url="https://t.me/tesyyai12345",
                    ),
                ],
            ]
        ),
    )
