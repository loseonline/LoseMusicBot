#
# Copyright (C) 2021-2022 by TeamLose@Github, < https://github.com/usermusti >.
#
# This file is part of < https://github.com/usermusti/LoseMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/usermusti/LoseMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from config import BANNED_USERS
from strings import get_command
from LoseMusic import app
from LoseMusic.utils.database import (get_playmode, get_playtype,
                                       is_nonadmin_chat)
from LoseMusic.utils.decorators import language
from LoseMusic.utils.inline.settings import playmode_users_markup

### Commands
PLAYMODE_COMMAND = get_command("PLAYMODE_COMMAND")


@app.on_message(
    filters.command(PLAYMODE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def playmode_(client, message: Message, _):
    playmode = await get_playmode(message.chat.id)
    if playmode == "Direct":
        Direct = True
    else:
        Direct = None
    is_non_admin = await is_nonadmin_chat(message.chat.id)
    if not is_non_admin:
        Group = True
    else:
        Group = None
    playty = await get_playtype(message.chat.id)
    if playty == "Everyone":
        Playtype = None
    else:
        Playtype = True
    buttons = playmode_users_markup(_, Direct, Group, Playtype)
    response = await message.reply_text(
        _["playmode_1"].format(message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
