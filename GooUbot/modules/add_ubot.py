import asyncio
import importlib
from datetime import datetime

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.raw import functions

from GooUbot import *
from GooUbot.core.helpers.inline import BTN

@bot.on_message(filters.regex("^Kembali$") & filters.private)
@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message): 
    buttons = BTN.START(message)
    msg = MSG.START(message)
    return await message.reply(msg, reply_markup=ReplyKeyboardMarkup(buttons))

@bot.on_message(filters.regex("^Status Akun$") & filters.private)
async def _(client, message):
    user_id = message.from_user.id
    if user_id in ubot._get_my_id:
        button = [
            [KeyboardButton("Kembali")],
        ]
        exp = await get_expired_date(user_id)
        prefix = await get_pref(user_id)
        waktu = exp.strftime("%d-%m-%Y") if exp else "None"
        return await message.reply(
            f"""
<blockquote>Keterangan Akun
  Status : Premium
  Prefix : {prefix[0]}
  Masa Aktif : {waktu}</b></blockquote>
""",
            reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)
        )
    else:
        button = [
            [KeyboardButton("Kembali")],
        ]
        return await message.reply(
            f"""
<blockquote><b>\u274c Sorry cuy lu belum beli userbot, beli dulu sana chat admin Goo.</b></blockquote>
""",
            reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)
    )

async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<blockquote>\u1d18\u1d07\u1d0d\u0299\u1d00\u1d1b\u1d00\u029f\u1d00\u0274 \u1d0f\u1d1b\u1d0f\u1d0d\u1d00\u1d1b\u026a\ua731!\n\u0274\u0262\u1d1c\u0274\u1d00\u1d0b\u1d00\u0274 /\ua731\u1d1b\u1d00\u0280\u1d1b \u1d1c\u0274\u1d1b\u1d1c\u1d0b \u1d0d\u1d07\u1d0d\u1d1c\u029f\u1d00\u026a \u1d1c\u029f\u1d00\u0274\u0262</blockquote>"
        )
        return True
    return False

@bot.on_message(filters.regex("^Pasang Userbot$") & filters.private)
async def _(client, message):
    user_id = message.from_user.id
    if user_id in ubot._get_my_id:
        button = [
            [KeyboardButton("Restart Ubot")],
            [KeyboardButton("Kembali")]
        ]
        return await message.reply(
            f"""You are already create this userbot. if userbot not working, click Restart Button.""", 
            reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        button = [
            [KeyboardButton("Kembali")]
        ]
        return await message.reply(
            f"""You can't create userbot!.\n\n Because Max Userbot is a {Fonts.smallcap(str(len(ubot._ubot)))}.\n\n Contact @goofounder to fix this problem.""",
            reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)
        )
    premium_users, ultra_premium_users = await get_list_from_vars(client.me.id, "PREM_USERS"), await get_list_from_vars(client.me.id, "ULTRA_PREM")
    if user_id not in premium_users and user_id not in ultra_premium_users:
        button = [
            [KeyboardButton("Contact Admin")],
            [KeyboardButton("Kembali")],
        ]
        return await message.reply(
            f"""
<blockquote><b>\u274c \u1d0d\u1d00\u1d00\ua730 \u1d00\u0274\u1d05\u1d00 \u0299\u1d07\u029f\u1d1c\u1d0d \u1d0d\u1d07\u1d0d\u0299\u1d07\u029f\u026a \u1d1c\ua731\u1d07\u0280\u0299\u1d0f\u1d1b, \ua731\u026a\u029f\u1d00\u1d0b\u1d00\u0274 \u1d0d\u1d07\u1d0d\u0299\u1d07\u029f\u026a \u1d1b\u1d07\u0280\u029f\u1d07\u0299\u026a\u029c \u1d05\u1d00\u029c\u1d1c\u029f\u1d1c</b></blockquote>
""",
            reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)
        )
    else:
        user_id = message.from_user.id
        await message.delete()
        await bot.send_message(
            user_id,
            "Kamu sudah mendapatkan akses. klik tombol di bawah untuk masukan nomor telegram",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("\ud83d\udcf1Send phone number", request_contact=True)]],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        try:
            phone = await bot.listen(user_id, filters=filters.contact, timeout=300)
        except asyncio.TimeoutError:
            return await bot.send_message(
                user_id,
                "<blockquote>\u1d18\u1d07\u1d0d\u0299\u1d00\u1d1b\u1d00\u029f\u1d00\u0274 \u1d0f\u1d1b\u1d0f\u1d0d\u1d00\u1d1b\u026a\ua731!\n\u0274\u0262\u1d1c\u0274\u1d00\u1d0b\u1d00\u0274 /start \u1d1c\u0274\u1d1b\u1d1c\u1d0b \u1d0d\u1d07\u1d0d\u1d1c\u029f\u1d00\u026a \u1d1c\u029f\u1d00\u0274\u0262</blockquote>"
            )

        if not phone.contact:
            return await bot.send_message(
                user_id,
                "\u274c Harap klik tombol untuk bagikan nomor, jangan ketik manual."
            )

        phone_number = phone.contact.phone_number
        new_client = Ubot(
            name=str(message.id),
            api_id=API_ID,
            api_hash=API_HASH,
            in_memory=False,
        )
        get_otp = await bot.send_message(
            user_id,
            "<blockquote><b>\u1d0d\u1d07\u0274\u0262\u026a\u0280\u026a\u1d0d \u1d0b\u1d0f\u1d05\u1d07 \u1d0f\u1d1b\u1d18...</b></blockquote>"
        )
        await new_client.connect()
        try:
            code = await new_client.send_code(phone_number.strip())
        except ApiIdInvalid as AID:
            await get_otp.delete()
            return await bot.send_message(user_id, AID)
        except PhoneNumberInvalid as PNI:
            await get_otp.delete()
            return await bot.send_message(user_id, PNI)
        except PhoneNumberFlood as PNF:
            await get_otp.delete()
            return await bot.send_message(user_id, PNF)
        except PhoneNumberBanned as PNB:
            await get_otp.delete()
            return await bot.send_message(user_id, PNB)
        except PhoneNumberUnoccupied as PNU:
            await get_otp.delete()
            return await bot.send_message(user_id, PNU)
        except Exception as error:
            await get_otp.delete()
            return await bot.send_message(user_id, f"ERROR: {error}")

        try:
            sent_code = {
                SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>akun telegram</a> resmi",
                SentCodeType.SMS: "sms anda",
                SentCodeType.CALL: "panggilan telpon",
                SentCodeType.FLASH_CALL: "pangilan kilat telepon",
                SentCodeType.FRAGMENT_SMS: "fragment sms",
                SentCodeType.EMAIL_CODE: "email anda",
            }
            await get_otp.delete()
            otp = await bot.ask(
                user_id,
                (
                    "<blockquote><b>silahkan periksa kode otp dari akun resmi telegram. kirim kode otp ke sini setelah membaca format di bawah ini.</b>\n"
                    "\nJika kode otp adalah <code>12345</code> tolong <b>[ tambahkan spasi ]</b> kirimkan seperti ini <code>1 2 3 4 5</code>\n"
                    "\n<b>gunakan /cancel untuk membatalkan proses membuat userbot</b></blockquote>"
                ),
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(
                user_id,
                "<blockquote>pembatalan otomatis!\ngunakan /start untuk memulai ulang</blockquote>"
            )

        if await is_cancel(message, otp.text):
            return

        otp_code = otp.text
        try:
            await new_client.sign_in(
                phone_number.strip(),
                code.phone_code_hash,
                phone_code=" ".join(str(otp_code)),
            )
        except PhoneCodeInvalid as PCI:
            return await bot.send_message(user_id, PCI)
        except PhoneCodeExpired as PCE:
            return await bot.send_message(user_id, PCE)
        except BadRequest as error:
            return await bot.send_message(user_id, f"ERROR: {error}")
        except SessionPasswordNeeded:
            try:
                two_step_code = await bot.ask(
                    user_id,
                    "akun anda telah mengaktifkan verifikasi dua langkah. silahkan kirimkan passwordnya.\n\ngunakan /cancel untuk membatalkan proses membuat userbot</b>",
                    timeout=300,
                )
            except asyncio.TimeoutError:
                return await bot.send_message(
                    user_id,
                    "<blockquote>pembatalan otomatis!\ngunakan /start untuk memulai ulang</blockquote>"
                )
            if await is_cancel(message, two_step_code.text):
                return
            new_code = two_step_code.text
            try:
                await new_client.check_password(new_code)
            except Exception as error:
                return await bot.send_message(user_id, f"ERROR: {error}")

        session_string = await new_client.export_session_string()
        await new_client.disconnect()
        new_client.storage.session_string = session_string
        new_client.in_memory = False
        bot_msg = await bot.send_message(
            user_id,
            "sedang memproses....\n\nsilahkan tunggu sebentar",
            disable_web_page_preview=True,
        )
        await new_client.start()
        if not user_id == new_client.me.id:
            ubot._ubot.remove(new_client)
            return await bot_msg.edit(
                "<blockquote><b>harap gunakan nomer telegram anda di akun anda saat ini dan bukan nomer telegram dari akun lain</b></blockquote>"
            )

        await add_ubot(
            user_id=int(new_client.me.id),
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_string,
        )

        for mod in loadModule():
            importlib.reload(importlib.import_module(f"GooUbot.modules.{mod}"))

        SH = await ubot.get_prefix(new_client.me.id)
        buttons = BTN.START(message)
        text_done = f"""
    <blockquote><b>berhasil diaktifkan
    name : <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a>
    id : {new_client.me.id}
    prefixes : {' '.join(SH)} 
    harap join : @nathsupport dan jangan out agar safety
    jika bot tidak respon, ketik /restart</b></blockquote>
            """
        await bot_msg.edit(
            text_done,
            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
        )
        await bash("rm -rf *session*")
        await install_my_peer(new_client)
        try:
            await new_client.join_chat("https://t.me/gooteam")
            await new_client.join_chat("https://t.me/tokogoo")
            await new_client.join_chat("https://t.me/goologs")   
            await new_client.join_chat("https://t.me/+JBP2m-xblhA3ODJl")
        except UserAlreadyParticipant:
            pass

        for chat_id in LOGS_MAKER_UBOT:
            try:
                await bot.send_message(
                    chat_id,
                    f"""<b>\u274f {bot.me.full_name} diaktifkan</b>
    <b>\u251c akun:</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
    <b>\u2570 id:</b> <code>{new_client.me.id}</code>
    """,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "cek masa aktif",
                                    callback_data=f"cek_masa_aktif {new_client.me.id}",
                                )
                            ],
                        ]
                    ),
                    disable_web_page_preview=True,
                )
            except Exception as e:
                print(f"GAGAL KIRIM KE {chat_id} : {e}")

@PY.BOT("control")
async def _(client, message):
    buttons = [
            [KeyboardButton("Restart Ubot")],
        ]
    await message.reply(
            f"""
<blockquote><b>anda akan melakukan restart?!\n\njika iya pencet tombol di bawah ini</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )

@bot.on_message(filters.regex("^Restart Ubot$") & filters.private)
async def _(client, message):
    if message.from_user.id not in ubot._get_my_id:
        return await message.answer(
            f"you don't have acces",
            True,
        )
    for X in ubot._ubot:
        if message.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"GooUbot.modules.{mod}")
                            )
                        return await message.reply(
                            f"restart berhasil dilakukan !\n\n name: {UB.me.first_name} {UB.me.last_name or ''} | {UB.me.id}"
                        )
                    except Exception as error:
                        return await message.reply(f"{error}")

@PY.BOT("restart")
async def _(client, message):
    msg = await message.reply("<b>tunggu sebentar</b>")
    if message.from_user.id not in ubot._get_my_id:
        return await msg.edit(
            f"you don't have acces",
            True,
        )
    for X in ubot._ubot:
        if message.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"GooUbot.modules.{mod}")
                            )
                        return await msg.edit(
                            f"restart berhasil dilakukan !\n\n name: {UB.me.first_name} {UB.me.last_name or ''} | `{UB.me.id}`"
                        )
                    except Exception as error:
                        return await msg.edit(f"{error}")

@bot.on_message(filters.regex("^Daftar Pengguna$") & filters.private )
@PY.BOT("getubot")
@PY.ADMIN
@PY.OWNER
async def _(client, message):
    await bot.send_message(
        message.from_user.id,
        await MSG.UBOT(0),
        reply_markup=InlineKeyboardMarkup(BTN.UBOT(ubot._ubot[0].me.id, 0)),
    )

@bot.on_message(filters.regex("^Syarat dan Ketentuan$") & filters.private)
async def _(client, message):
    await message.reply(f"""
<blockquote><b>Hai cuy, nih gua jelasin apa itu userbot sama apa resiko kalo lu make userbot. Baca nih!

Userbot itu bot yang bisa di pasang ke akun lu, fungsi sama tujuan nya juga beda beda. Tapi yang pasti userbot biasanya di pake buat jadi asisten pribadi gtu yang mempermudah lu lakuin sesuatu.

Resiko masang userbot juga beragam, mulai dari kena limit, freeze, sampe bisa ke banned tergantung ketahanan akun. yang rawan kedeak itu biasanya ID awalan 6-8(10digit) atau akun akun yang baru di bikin. Belakagan ini banyak yang kedeak karna ketentuan dari pihak Telegram makin di perketat, soalnya userbot itu bisa di bilang ngelanggar Kebijkan Telegram. Jadi, mau akun baru atau lama sama aja punya potensi ke banned, ya tergantung cara lu make userbot nya aja sih.

Buat ngurangin resiko nya, lu bisa pake ID lama kaya 1/2/3/4/5(10digit) apa ga akun yang lebih lama lagi yaitu akun 9 digit. Kalo ID 6/7/8 lu harus pake dulu akun nya minimal sebulan lah, ya walaupun sebenernya ke banned apa ngga nya itu ya tergantung dari sistem & pihak Telegram nya juga. Terakhir nih, biar lu ga gampang kena limit lu bisa berlangganan Telegram Premium.

Penyebab kena Banned/Limit :
1. Kedeteksi spam
2. Kedeteksi ngelanggan Kebijakan Telegram
3. Banyak yang report akun lu

Udah si gitu aja dari gua, byee!</b></blockquote>
"""
    )

@bot.on_message(filters.regex("^Informasi Bot$") & filters.private)
async def _(client, message):
    await message.reply(f"""{bot.me.mention} version 1.2 by @goofounder
"""
    )

@bot.on_message(filters.regex("^Support Group$") & filters.private)
async def _(client, message):
    await message.reply(f"""Join sini buat nanya nanya seputar bot. 
Group : https://t.me/gooteam
"""
    )
    
@bot.on_message(filters.regex("^Lihat Fitur$") & filters.private)
async def _(client, message):
    btn = [
        [InlineKeyboardButton("Ayo tekan akuu!!", callback_data="help_back")]
    ]
    await message.reply(f"Hayo mau liat apa?", reply_markup=InlineKeyboardMarkup(btn))

@PY.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f"\u23f3 tinggal {xxxx} hari lagi", True)
    except Exception as e:
        return await callback_query.answer("\u2705 sudah tidak aktif", True)

@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
        return await callback_query.answer(
            f"\u274c tombol ini bukan untuk mu {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"{get_id}"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"{get_id}"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            await remove_ubot(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await callback_query.answer(
                f"\u2705 {get_mention} berhasil dihapus dari database", True
            )
            await callback_query.edit_message_text(
                await MSG.UBOT(0),
                reply_markup=InlineKeyboardMarkup(
                    BTN.UBOT(ubot._ubot[0].me.id, 0)
                ),
            )
            await bot.send_message(
                X.me.id,
                MSG.EXP_MSG_UBOT(X),
                reply_markup=InlineKeyboardMarkup(BTN.EXP_UBOT()),
            )

    
@PY.CALLBACK("^(p_ub|n_ub)")
async def _(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "n_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "p_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.UBOT(count),
        reply_markup=InlineKeyboardMarkup(
            BTN.UBOT(ubot._ubot[count].me.id, count)
        ),
    )

@PY.CALLBACK("^(get_otp|get_phone|get_faktor|ub_deak|deak_akun)")
async def tools_userbot(client, callback_query):
    user_id = callback_query.from_user.id
    query = callback_query.data.split()
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"\u274c tombol ini bukan untuk mu {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    X = ubot._ubot[int(query[1])]
    if query[0] == "get_otp":
        async for otp in X.search_messages(777000, limit=1):
            try:
                if not otp.text:
                    await callback_query.answer("\u274c kode otp tidak ditemukan", True)
                else:
                    await callback_query.edit_message_text(
                        otp.text,
                        reply_markup=InlineKeyboardMarkup(
                            BTN.UBOT(X.me.id, int(query[1]))
                        ),
                    )
                    await X.delete_messages(X.me.id, otp.id)
            except Exception as error:
                return await callback_query.answer(error, True)
    elif query[0] == "get_phone":
        try:
            return await callback_query.edit_message_text(
                f"<blockquote><b>\ud83d\udcf2 nomer telepon dengan user_id <code>{X.me.id}</code> adalah <code>{X.me.phone_number}</code></b></blockquote>",
                reply_markup=InlineKeyboardMarkup(
                    BTN.UBOT(X.me.id, int(query[1]))
                ),
            )
        except Exception as error:
            return await callback_query.answer(error, True)
    elif query[0] == "get_faktor":
        code = await X.get_two_factor(X.me.id)
        if code == None:
            return await callback_query.answer(
                "\ud83d\udd10 kode two-factor authentication tidak ditemukan", True
            )
        else:
            return await callback_query.edit_message_text(
                f"<b>\ud83d\udd10 two-factor authentication dengan user_id <code>{X.me.id}</code> adalah <code>{code}</code></b>",
                reply_markup=InlineKeyboardMarkup(
                    BTN.UBOT(X.me.id, int(query[1]))
                ),
            )
    elif query[0] == "ub_deak":
        return await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(BTN.DEAK(X.me.id, int(query[1])))
        )
    elif query[0] == "deak_akun":
        ubot._ubot.remove(X)
        await X.invoke(functions.account.DeleteAccount(reason="madarchod hu me"))
        return await callback_query.edit_message_text(
            MSG.DEAK(X),
            reply_markup=InlineKeyboardMarkup(BTN.UBOT(X.me.id, int(query[1]))),
    )
