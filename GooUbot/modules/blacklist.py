__MODULE__ = "bl"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴀᴄᴋʟɪsᴛ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}addbl</code>
🦠 ᴋᴇᴛ : ᴍᴀꜱᴜᴋᴀɴ ɢʀᴏᴜᴘ ᴋᴇ ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}unbl</code>
🦠 ᴋᴇᴛ : ʜᴀᴍᴜꜱ ɢʀᴏᴜᴘ ᴋᴇ ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}listbl</code>
🦠 ᴋᴇᴛ : ʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ɢʀᴏᴜᴘ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}rallbl</code>
🦠 ᴋᴇᴛ : ʜᴀᴍᴜꜱ ꜱᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴋᴇ ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
"""

from GooUbot import *

@PY.UBOT("addbl")
@PY.IDOL("caddbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    _msg = f"<blockquote><b>{prs} ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ...</b></blockquote>"

    msg = await message.reply(_msg)
    try:
        chat_id = message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id in blacklist:
            txt = f"""
<blockquote><b>\u232d {grp} \u0262\u0280\u1d0f\u1d1c\u1d18: {message.chat.title}</blockquote></b>
<blockquote><b>\u232d {ktrn} \u1d0b\u1d07\u1d1b: s\u1d1c\u1d05\u1d00\u029c \u1d00\u1d05\u1d00 \u1d05\u1d00\u029f\u1d00\u1d0d \u029f\u026as\u1d1b</blockquote></b>
"""
        else:
            await add_to_vars(client.me.id, "BL_ID", chat_id)
            txt = f"""
<blockquote><b>\u232d {grp} \u0262\u0280\u1d0f\u1d1c\u1d18: {message.chat.title}</blockquote></b>\n<blockquote><b>\u232d {ktrn} \u1d0b\u1d07\u1d1b: \u0299\u1d07\u0280\u029c\u1d00s\u026a\u029f \u1d05\u026a \u1d1b\u1d00\u1d0d\u0299\u1d00\u029c\u1d0b\u1d00\u0274 \u1d0b\u1d07 \u1d05\u1d00\u029f\u1d00\u1d0d \u029f\u026as\u1d1b \u1d0a\u1d07\u1d0d\u0299\u1d0f\u1d1b</blockquote></b>
"""

        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("unbl")
@PY.IDOL("cunbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}proce\ua731\ua731ing..."

    msg = await message.reply(_msg)
    try:
        chat_id = get_arg(message) or message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id not in blacklist:
            response = f"""
<blockquote><b>\u232d {grp} \u0262\u0280\u1d0f\u1d1c\u1d18: {message.chat.title}</blockquote></b>
<blockquote><b>\u232d {ktrn} \u1d0b\u1d07\u1d1b: \u1d1b\u026a\u1d05\u1d00\u1d0b \u1d00\u1d05\u1d00 \u1d05\u1d00\u029f\u1d00\u1d0d \u029f\u026as\u1d1b </b></blockquote>
"""
        else:
            await remove_from_vars(client.me.id, "BL_ID", chat_id)
            response = f"""
<blockquote><b>\u232d {grp} \u0262\u0280\u1d0f\u1d1c\u1d18: {message.chat.title}</blockquote ></b>
<blockquote><b>\u232d {ktrn} \u1d0b\u1d07\u1d1b: \u0299\u1d07\u0280\u029c\u1d00s\u026a\u029f \u1d05\u026a \u029c\u1d00\u1d18\u1d1cs \u1d0b\u1d07 \u1d05\u1d00\u029f\u1d00\u1d0d \u029f\u026as\u1d1b </blockquote></b>
"""

        return await msg.edit(response)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("listbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}proce\ua731\ua731ing..."
    mzg = await message.reply(_msg)

    blacklist = await get_list_from_vars(client.me.id, "BL_ID")
    total_blacklist = len(blacklist)

    list = f"{brhsl} \u1d05\u1d00\ua730\u1d1b\u1d00\u0280 \u0299\u029f\u1d00\u1d04\u1d0b\u029f\u026a\ua731\u1d1b\n"

    for chat_id in blacklist:
        try:
            chat = await client.get_chat(chat_id)
            list += f" \u251c {chat.title} | {chat.id}\n"
        except Exception as e:
            list += f" \u251c {chat_id}\n"

    list += f"{ktrng} \u1d1b\u1d0f\u1d1b\u1d00\u029f \u0299\u029f\u1d00\u1d04\u1d0b\u029f\u026a\ua731\u1d1b : {total_blacklist}"
    return await mzg.edit(list)


@PY.UBOT("rallbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    _msg = f"{prs} \u1d18\u0280\u1d0f\u1d04\u1d07\ua731\ua731\u026a\u0274\u0262..."

    msg = await message.reply(_msg)
    blacklists = await get_list_from_vars(client.me.id, "BL_ID")

    if not blacklists:
        return await msg.edit(f"{ggl} \u0299\u029f\u1d00\u1d04\u1d0b\u029f\u026a\ua731\u1d1b \u0299\u0280\u1d0f\u1d00\u1d05\u1d04\u1d00\ua731\u1d1b \u1d00\u0274\u1d05\u1d00 \u1d0b\u1d0f\ua731\u1d0f\u0274\u0262.")

    for chat_id in blacklists:
        await remove_from_vars(client.me.id, "BL_ID", chat_id)

    await msg.edit(f"{brhsl} \ua731\u1d07\u1d0d\u1d1c\u1d00 \u0299\u029f\u1d00\u1d04\u1d0b\u029f\u026a\ua731\u1d1b \u0299\u0280\u1d0f\u1d00\u1d05\u1d04\u1d00\ua731\u1d1b \u0299\u1d07\u0280\u029c\u1d00\ua731\u026a\u029f \u1d05\u026a \u029c\u1d00\u1d18\u1d1c\ua731.")
