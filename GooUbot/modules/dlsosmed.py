import asyncio
from pyrogram import Client
from pyrogram.types import Message
import os
from GooUbot import *

__MODULE__ = "download"
__HELP__ = """
<blockquote><b>--bantuan untuk download--</b></blockquote>

<blockquote><b>\ud83d\udea6 perintah : <code>{0}dl [link]</code>
\ud83e\udda0 ket : mendownload video sosmed via link.</b></blockquote>
"""

@PY.UBOT("dl")
@PY.TOP_CMD
async def download_video(client: Client, message: Message):
    if not (args := message.text.split(maxsplit=1)[1:]):
        return await message.reply("\u274c Kirimkan link video!\n\nContoh: <code>.dl https://tiktok.com/xxx</code>")
    
    url = args[0]
    await message.reply("\ud83d\udd04 Mendownload...")

    filename = "video.mp4"
    try:
        process = await asyncio.create_subprocess_exec(
            "yt-dlp", "-o", filename, url,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if not os.path.exists(filename):
            return await message.reply("\u274c Gagal mengunduh video.")

        await client.send_video(
            chat_id=message.chat.id,
            video=filename,
            caption="\u2705 Video berhasil diunduh!",
            reply_to_message_id=message.id
        )
        os.remove(filename)
    except Exception as e:
        await message.reply(f"\u274c Error: {e}")
