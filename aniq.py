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

from random import choice

from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class AnimatedQuotesMod(loader.Module):
    """Simple module to create animated stickers via bot"""

    strings = {
        "name": "Module---[AnimatedQuotes]",
        "no_text": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Provide a text to"
            " create sticker with</b>"
        ),
        "processing": (
            "<emoji document_id=5451646226975955576>⌛️</emoji> <b>Processing...</b>"
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
        "_cmd_doc_aniq": "<text> - Создать анимированный стикер",
        "_cls_doc": "Простенький модуль, который создает анимированные стикеры",
    }

    async def aniqcmd(self, message: Message):
        """<text> - Create animated quote"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_text"))
            return

        message = await utils.answer(message, self.strings("processing"))

        try:
            query = await self._client.inline_query("@QuotAfBot", args)
            chosen_sticker = choice(query[1:3])
            await message.respond(file=chosen_sticker.document)
        except Exception as e:
            await utils.answer(message, str(e))
            return

        if message.out:
            await message.delete()
