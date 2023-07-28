#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://static.hikari.gay/aniquotes_icon.png
# meta banner: https://mods.hikariatama.ru/badges/aniquotes.jpg
# meta developer: @Mmazzerratti
# scope: hikka_only
# scope: hikka_min 1.2.10

from telethon.tl.types import Message

from .. import loader, utils

import traceback

from io import StringIO

import sys

@loader.tds
class AnimatedQuotesMod(loader.Module):
    """Simple module to create animated stickers via bot"""

    strings = {
        "name": "Module [Exec]",
        "exec": (
            "Exec"
        ),
    }

    strings_ru = {
        "no_text": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Укажи текст для"
            " создания стикера</b>"
        ),
        "processing": (
            "<emoji document_id=5451646226975955576>⌛️</emoji> <b>Обработка...</b>"
        ),
        "_cmd_doc_exec": "<code> - Выполняет команду",
        "_cls_doc": "Простенький модуль, который выполняет команды",
    }

    async def execcmd(self, message: Message):
        code = utils.get_args_raw(message)
        if code:
            try:
                output = sys.stdout = StringIO()
                exec(code)
                val = output.getvalue()
                if val.strip():
                    await utils.answer(message, f"👥 Команда:\n{code}\n\n📤 Вывод:\n{output.getvalue()}")
            except:
                await utils.answer(message, traceback.format_exc())
