__MODULE__ = "carbon"
__HELP__ = """
<blockquote><b>--\u0299\u1d00\u0274\u1d1b\u1d1c\u1d00\u0274 \u1d1c\u0274\u1d1b\u1d1c\u1d0b \u1d04\u1d00\u0280\u0299\u1d0f\u0274--</b></blockquote>

<blockquote><b>\ud83d\udea6 \u1d18\u1d07\u0280\u026a\u0274\u1d1b\u1d00\u029c :</b> <code>{0}carbon</code>
\ud83e\udda0 \u1d0b\u1d07\u1d1b : \u1d0d\u1d07\u1d0d\u0299\u1d1c\u1d00\u1d1b \u1d1b\u1d07x\u1d1b \u1d04\u1d00\u0280\u0299\u1d0f\u0274\u1d00\u0280\u1d00.</b></blockquote>
"""

import asyncio

from io import BytesIO
from GooUbot import *

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@PY.UBOT("carbon")
@PY.TOP_CMD
async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.reply("mempro\ua731e\ua731...")
    carbon = await make_carbon(text)
    await ex.edit("uploading...")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"carboni\ua731ed by :{client.me.mention}",
        ),
    )
    carbon.close()
