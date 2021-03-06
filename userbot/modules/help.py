# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**`Command Tidak Ditemukan, Harap Ketik Command Dengan Benar`**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t â  "
        await event.edit("**ð¹à½ ÖÊÒ½-Ô±ÊÒ½É¾ÒÖÕ§ð¹**\n\n"
                         f"**â Bá´á´ á´ê° {DEFAULTUSER}**\n**â Má´á´á´Êá´ê± : {len(modules)}**\n\n"
                         "**â¢ Má´ÉªÉ´ Má´É´á´ :**\n"
                         f"â {string}â\n\n")
        await event.reply(f"\nâ£ï¸ **Perintah Untuk Melihat Modules** â£ï¸\n\nð¾ð¤ð¢ð¢ðð£ð: >`.help animasi1`\nð¾ð¤ð¢ð¢ðð£ð: >`.helpme`\n\nð  **Perintah Diatas Wajib Kalian Tau** ð ")
        await asyncio.sleep(1000)
        await event.delete()
