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

import asyncio

import random

from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class AnimatedQuotesMod(loader.Module):
    """Simple module to create animated stickers via bot"""

    strings = {
        "name": "Module [AnimatedQuotes]",
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

        retries = 3
        for attempt in range(retries):
            try:
                message_processing = await utils.answer(message, self.strings("processing"))
                query = await self._client.inline_query("@QuotAfBot", args)
                await message_processing.delete()

                if not query:
                    await utils.answer(message, self.strings("no_results"))
                    return

                if len(query) >= 2:
                    selected_result = random.choice([query[1], query[2]])
                else:
                    selected_result = query[0]

                await message.respond(file=selected_result.document)
                return

            except Exception as e:
                error_msg = str(e)
                if "The message cannot be empty unless a file is provided" not in error_msg:
                    await utils.answer(message, error_msg)
                    return

                await asyncio.sleep(1)

        await utils.answer(message, "Failed to create animated quote. Please try again later.")

        if message.out:
            await message.delete()
