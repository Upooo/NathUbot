from geopy.geocoders import Nominatim
from GooUbot import *

__MODULE__ = "gmaps"
__HELP__ = """
<blockquote><b>--bantuan untuk gmaps--</b></blockquote>

<blockquote><b>\ud83d\udea6 perintah : <code>{0}gps</code> [lokasi]
\ud83e\udda0 ket : mencari tempat melalui google maps / gps.</b></blockquote>
"""

@PY.UBOT("gps|maps")
async def gps(client, message):
    input_str = message.text.split(" ", 1)
    if len(input_str) < 2:
        return await message.reply("<blockquote><b>Mohon berikan tempat yang dicari.</b></blockquote>")
    input_str = input_str[1]
    await message.reply("<blockquote><b>Menemukan lokasi ini di server map...</b></blockquote>")
    geolocator = Nominatim(user_agent="bot")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await message.reply_location(latitude=lat, longitude=lon)
    else:
        await message.reply("<blockquote><b>Saya tidak dapat menemukannya.</b></blockquote>")
