from GooUbot import *
from pyrogram.raw.functions.contacts import GetBlocked

__MODULE__ = "blocked"
__HELP__ = """
<blockquote><b>--\u0299\u1d00\u0274\u1d1b\u1d1c\u1d00\u0274 \u1d1c\u0274\u1d1b\u1d1c\u1d0b \u0299\u029f\u1d0f\u1d04\u1d0b\u1d07\u1d05--</b></blockquote>

<blockquote><b>\ud83d\udea6 \u1d18\u1d07\u0280\u026a\u0274\u1d1b\u1d00\u029c :</b> <code>{0}unblockall</code>
\ud83e\udda0 \u1d0b\u1d07\u1d1b : \u1d1c\u0274\u0299\u029f\u1d0f\u1d04\u1d0b \ua731\u1d07\u1d0d\u1d1c\u1d00 \u1d1c\ua731\u1d07\u0280 \u1d05\u026a \u1d05\u1d00\ua730\u1d1b\u1d00\u0280 \u1d04\u1d0f\u0274\u1d1b\u1d00\u1d04\u1d1b.</b></blockquote>
<blockquote><b>\ud83d\udea6 \u1d18\u1d07\u0280\u026a\u0274\u1d1b\u1d00\u029c :</b> <code>{0}getblock</code>
\ud83e\udda0 \u1d0b\u1d07\u1d1b : \u029f\u026a\u029c\u1d00\u1d1b \u1d0a\u1d1c\u1d0d\u029f\u1d00\u029c \u028f\u1d00\u0274\u0262 \u1d05\u026a \u0299\u029f\u1d0f\u1d04\u1d0b\u026a\u0280 \u1d05\u026a \u1d04\u1d0f\u0274\u1d1b\u1d00\u1d04\u1d1b.</b></blockquote>
"""

@PY.UBOT("unblockall")
async def _(user, message):
    sks = await EMO.BERHASIL(user)
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"<blockquote><b>{prs} \u1d1b\u1d1c\u0274\u0262\u0262\u1d1c \u0299\u1d07\u0274\u1d1b\u1d00\u0280...</b></blockquote>")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    for x in user_ids:
        try:
            await user.unblock_user(x)
        except Exception as e:
            pass
    await _prs.edit(f"<blockquote><b>{sks} \u0299\u1d07\u0280\u029c\u1d00\ua731\u026a\u029f \u1d0d\u1d07\u029f\u1d00\u1d0b\u1d1c\u1d0b\u1d00\u0274 \u1d1c\u0274\u0299\u029f\u1d0f\u1d04\u1d0b\u1d00\u029f\u029f \u1d1c\ua731\u1d07\u0280\ua731</b></blockquote>")

@PY.UBOT("getblock")
async def _(user, message):
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"<blockquote><b>{prs} \u1d1b\u1d1c\u0274\u0262\u0262\u1d1c \u0299\u1d07\u0274\u1d1b\u1d00\u0280...</b></blockquote>")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    teko = len(user_ids)
    if user_ids:
        try:
            await _prs.edit(f"<blockquote><b>\u1d0b\u1d00\u1d0d\u1d1c \u1d0d\u1d07\u1d0d\u0299\u029f\u1d0f\u1d04\u1d0b\u026a\u0280 : {teko} \u1d1c\ua731\u1d07\u0280\ua731</b></blockquote>")
        except Exception as i:
            await _prs.edit(f"{i}")
    else:
        await _prs.edit(f"\u1d1b\u026a\u1d05\u1d00\u1d0b \u1d00\u1d05\u1d00 \u028f\u1d00\u0274\u0262 \u1d05\u026a \u0299\u029f\u1d0f\u1d04\u1d0b\u026a\u0280")
