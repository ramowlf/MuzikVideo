#
# Copyright (C) 2023-2024 by YukkiOwner@Github, < https://github.com/YukkiOwner >.
#
# This file is part of < https://github.com/YukkiOwner/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YukkiOwner/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""


**Grup:** {message.chat.title} [`{message.chat.id}`]
**Üye Sayısı: 👉{sayı}**
**Kullanıcı:** {message.from_user.mention}
**Kullanıcı Adı:** @{message.from_user.username}
**Kullanıcı ID:** `{message.from_user.id}`
**Grup Linki:** {chatusername}
**Sorgu:** {message.text}

**Toplam Grup Sayısı: 👉{toplamgrup}**
**Aktif Ses: 👉{aktifseslisayısı}**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
                await app.set_chat_title(LOG_GROUP_ID, f"PLUTO MÜZİK LOG - {aktifseslisayısı}")
            except:
                pass
        return
