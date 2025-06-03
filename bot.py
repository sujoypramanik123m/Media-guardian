import os
import asyncio
from aiohttp import web
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, DELETE_DELAY

bot = Client("media_delete_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

MEDIA_TYPES = ["photo", "video", "audio", "document", "animation", "sticker"]

@bot.on_message(filters.group & filters.media)
async def auto_delete_media(client: Client, message: Message):
    if any(getattr(message, media_type, None) for media_type in MEDIA_TYPES):
        try:
            await asyncio.sleep(DELETE_DELAY)
            await message.delete()
        except Exception as e:
            print(f"Failed to delete message: {e}")

@bot.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    await message.reply_photo(
        photo="https://envs.sh/HcV.jpg",
        caption=f"""**┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼──────•
┆✦ » ʜᴇʏ {message.from_user.mention}
└──────────────────────•
✦ » ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ ᴍᴇᴅɪᴀ ɢᴜᴀʀᴅɪᴀɴ ʙᴏᴛ.
✦ » ɪ ᴡɪʟʟ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴇᴅɪᴀ ᴍᴇssᴀɢᴇs ᴀғᴛᴇʀ 𝟷𝟻 ᴍɪɴᴜᴛᴇs ɪɴ ɢʀᴏᴜᴘ
✦ » ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ, ɢɪᴠᴇ ᴍᴇ ᴏɴʟʏ ᴅᴇʟᴇᴛᴇ ᴘᴏᴡᴇʀ ᴀɴᴅ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ.

•──────────────────────•
❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ ➪ [˹ ʙᴏᴛᴍɪɴᴇ-ᴛᴇᴄʜ ˼](https://t.me/BOTMINE_TECH)
•──────────────────────•""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url=f"https://t.me/{client.me.username}?startgroup=true")],
            [
                InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/ll_RADHE7_ll"),
                InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/BOTMINE_TECH")
            ],
            [
                InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/BOTMINE_SUPPORT"),
                InlineKeyboardButton("˹ ᴍᴜsɪᴄ ʙᴏᴛ ˼", url="https://t.me/RADHE_MUSIC_ROBOT")
            ]
        ])
    )

async def handle(request):
    return web.Response(text="Bot is running")

async def start_webserver():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Dummy webserver started on port {port}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_webserver())
    bot.run()
