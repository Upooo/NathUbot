import asyncio
import platform
import time
import os
import psutil
from datetime import datetime

from GooUbot import *
from GooUbot.config import GooTeam

__MODULE__ = "nathtools"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴀᴛʜᴛᴏᴏʟꜱ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}sysinfo</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ɪɴꜰᴏ ꜱᴇʀᴠᴇʀ/ᴠᴘꜱ ʟᴇɴɢᴋᴀᴘ.</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}nath</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ᴘʀᴏꜰɪʟ ʙᴏᴛ ᴅᴀɴ ꜱᴛᴀᴛɪꜱᴛɪᴋ.</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}speedtest</code>
🦠 ᴋᴇᴛ : ᴛᴇꜱ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ɪɴᴛᴇʀɴᴇᴛ ꜱᴇʀᴠᴇʀ.</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}storage</code>
🦠 ᴋᴇᴛ : ᴄᴇᴋ ᴘᴇɴɢɢᴜɴᴀᴀɴ ꜱᴛᴏʀᴀɢᴇ ᴠᴘꜱ.</b></blockquote>
"""

_NATH_START = time.time()

NATH_LOGO = """
<code>
╔═══════════════════════════╗
║   ░█▄░█ ▄▀█ ▀█▀ █░█      ║
║   ░█░▀█ █▀█ ░█░ █▀█      ║
║   ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌     ║
║     ᴜ ꜱ ᴇ ʀ ʙ ᴏ ᴛ       ║
╚═══════════════════════════╝
</code>"""


def _bytes_to_human(n):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def _seconds_to_human(seconds):
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    parts = []
    if days > 0:
        parts.append(f"{days}ʜ")
    if hours > 0:
        parts.append(f"{hours}ᴊ")
    if minutes > 0:
        parts.append(f"{minutes}ᴍ")
    parts.append(f"{secs}ᴅ")
    return " ".join(parts)


def _progress_bar(percent, length=10):
    filled = int(length * percent / 100)
    bar = "█" * filled + "░" * (length - filled)
    return bar


@PY.UBOT("sysinfo")
@PY.TOP_CMD
async def sysinfo_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    msg = await message.reply(f"<b>{prs} ᴍᴇɴɢᴀᴍʙɪʟ ɪɴꜰᴏ ꜱᴇʀᴠᴇʀ...</b>")

    try:
        # CPU Info
        cpu_count = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq()
        cpu_percent = psutil.cpu_percent(interval=1)

        # Memory Info
        mem = psutil.virtual_memory()
        mem_used = _bytes_to_human(mem.used)
        mem_total = _bytes_to_human(mem.total)
        mem_bar = _progress_bar(mem.percent)

        # Disk Info
        disk = psutil.disk_usage("/")
        disk_used = _bytes_to_human(disk.used)
        disk_total = _bytes_to_human(disk.total)
        disk_bar = _progress_bar(disk.percent)

        # System Info
        uptime = time.time() - psutil.boot_time()
        bot_uptime = time.time() - _NATH_START
        py_version = platform.python_version()
        os_info = f"{platform.system()} {platform.release()}"

        text = f"""
{NATH_LOGO}
<blockquote><b>⚙️ ꜱᴇʀᴠᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b></blockquote>

<blockquote><b>🖥️ ᴏꜱ :</b> <code>{os_info}</code>
<b>🐍 ᴘʏᴛʜᴏɴ :</b> <code>{py_version}</code>
<b>⚡ ᴄᴘᴜ :</b> <code>{cpu_count} ᴄᴏʀᴇ(ꜱ) @ {cpu_freq.current:.0f}ᴍʜᴢ</code>
<b>📊 ᴄᴘᴜ ᴜꜱᴀɢᴇ :</b> <code>{cpu_percent}%</code></blockquote>

<blockquote><b>💾 ʀᴀᴍ :</b> <code>{mem_used} / {mem_total}</code>
<code>{mem_bar} {mem.percent}%</code></blockquote>

<blockquote><b>💿 ᴅɪꜱᴋ :</b> <code>{disk_used} / {disk_total}</code>
<code>{disk_bar} {disk.percent}%</code></blockquote>

<blockquote><b>⏱️ ꜱᴇʀᴠᴇʀ ᴜᴘᴛɪᴍᴇ :</b> <code>{_seconds_to_human(uptime)}</code>
<b>🤖 ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :</b> <code>{_seconds_to_human(bot_uptime)}</code></blockquote>

<b>{brhsl} ɴᴀᴛʜ ᴜꜱᴇʀʙᴏᴛ</b>
"""
        await msg.edit(text)
    except Exception as e:
        await msg.edit(f"<b>❌ Error:</b> <code>{e}</code>")


@PY.UBOT("nath")
@PY.TOP_CMD
async def nath_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    bot_uptime = _seconds_to_human(time.time() - _NATH_START)

    ubot_count = len(client._ubot) if hasattr(client, '_ubot') else 1
    me = client.me

    text = f"""
{NATH_LOGO}
<blockquote><b>{brhsl} ɴᴀᴛʜ ᴜꜱᴇʀʙᴏᴛ ᴠ𝝎.𝟎</b></blockquote>

<blockquote><b>👤 ᴜꜱᴇʀ :</b> {me.mention}
<b>🆔 ɪᴅ :</b> <code>{me.id}</code>
<b>📛 ᴜꜱᴇʀɴᴀᴍᴇ :</b> @{me.username or 'ᴛɪᴅᴀᴋ ᴀᴅᴀ'}
<b>🤖 ᴜʙᴏᴛ ᴀᴋᴛɪꜰ :</b> <code>{ubot_count}</code></blockquote>

<blockquote><b>⏱️ ᴜᴘᴛɪᴍᴇ :</b> <code>{bot_uptime}</code>
<b>🐍 ᴘʏᴛʜᴏɴ :</b> <code>{platform.python_version()}</code>
<b>📅 ᴅᴀᴛᴇ :</b> <code>{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</code></blockquote>

<blockquote><b>📝 ᴅᴇꜱᴋʀɪᴘꜱɪ :</b>
<i>ɴᴀᴛʜ ᴜꜱᴇʀʙᴏᴛ — ꜰᴀꜱᴛ, ꜱᴛᴀʙʟᴇ, ᴀɴᴅ ᴍᴜʟᴛɪ-ᴄʟɪᴇɴᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴜꜱᴇʀʙᴏᴛ.
ʙᴜɪʟᴛ ᴡɪᴛʜ ᴘʏʀᴏɢʀᴀᴍ & ᴘʏᴛɢᴄᴀʟʟꜱ.</i></blockquote>
"""
    await message.reply(text)


@PY.UBOT("speedtest|st")
@PY.TOP_CMD
async def speedtest_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    msg = await message.reply(f"<b>{prs} ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ꜱᴘᴇᴇᴅᴛᴇꜱᴛ...</b>")

    try:
        # Simple speed test using download from a known fast server
        test_url = "http://speedtest.tele2.net/1MB.zip"
        start_time = time.time()

        async with aiosession.get(test_url) as resp:
            data = await resp.read()
            download_time = time.time() - start_time
            file_size = len(data)

        download_speed = (file_size / download_time) / (1024 * 1024)  # MB/s
        download_speed_mbps = download_speed * 8  # Mbps

        # Ping test
        ping_start = time.time()
        async with aiosession.get("https://www.google.com", timeout=10) as resp:
            await resp.read()
        ping = (time.time() - ping_start) * 1000  # ms

        text = f"""
<blockquote><b>🚀 ꜱᴘᴇᴇᴅᴛᴇꜱᴛ ʀᴇꜱᴜʟᴛ</b></blockquote>

<blockquote><b>📥 ᴅᴏᴡɴʟᴏᴀᴅ :</b> <code>{download_speed:.2f} MB/s ({download_speed_mbps:.1f} Mbps)</code>
<b>🏓 ᴘɪɴɢ :</b> <code>{ping:.1f} ms</code>
<b>📦 ᴛᴇꜱᴛ ꜰɪʟᴇ :</b> <code>{_bytes_to_human(file_size)}</code></blockquote>

<b>{brhsl} ɴᴀᴛʜ ᴜꜱᴇʀʙᴏᴛ</b>
"""
        await msg.edit(text)
    except Exception as e:
        await msg.edit(f"<b>❌ ꜱᴘᴇᴇᴅᴛᴇꜱᴛ ɢᴀɢᴀʟ:</b> <code>{e}</code>")


@PY.UBOT("storage|disk")
@PY.TOP_CMD
async def storage_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    msg = await message.reply(f"<b>{prs} ᴍᴇɴɢᴇᴄᴇᴋ ꜱᴛᴏʀᴀɢᴇ...</b>")

    try:
        disk = psutil.disk_usage("/")
        disk_used = _bytes_to_human(disk.used)
        disk_free = _bytes_to_human(disk.free)
        disk_total = _bytes_to_human(disk.total)
        disk_bar = _progress_bar(disk.percent, 20)

        # Get top 5 largest directories in home
        home = os.path.expanduser("~")
        dir_sizes = []
        try:
            for item in os.listdir(home):
                path = os.path.join(home, item)
                if os.path.isdir(path):
                    total_size = 0
                    for dirpath, dirnames, filenames in os.walk(path):
                        for fname in filenames:
                            fp = os.path.join(dirpath, fname)
                            try:
                                total_size += os.path.getsize(fp)
                            except OSError:
                                pass
                    dir_sizes.append((item, total_size))
        except Exception:
            pass

        dir_sizes.sort(key=lambda x: x[1], reverse=True)
        top_dirs = dir_sizes[:5]

        dir_text = ""
        for name, size in top_dirs:
            dir_text += f"├ <code>{name}/</code> — {_bytes_to_human(size)}\n"

        text = f"""
<blockquote><b>💿 ꜱᴛᴏʀᴀɢᴇ ɪɴꜰᴏ</b></blockquote>

<blockquote><b>📊 ᴛᴏᴛᴀʟ :</b> <code>{disk_total}</code>
<b>📦 ᴛᴇʀᴘᴀᴋᴀɪ :</b> <code>{disk_used} ({disk.percent}%)</code>
<b>📭 ᴛᴇʀꜱɪꜱᴀ :</b> <code>{disk_free}</code>

<code>{disk_bar}</code></blockquote>

<blockquote><b>📂 ᴛᴏᴘ ᴅɪʀᴇᴄᴛᴏʀʏ :</b>
{dir_text}</blockquote>

<b>{brhsl} ɴᴀᴛʜ ᴜꜱᴇʀʙᴏᴛ</b>
"""
        await msg.edit(text)
    except Exception as e:
        await msg.edit(f"<b>❌ Error:</b> <code>{e}</code>")
