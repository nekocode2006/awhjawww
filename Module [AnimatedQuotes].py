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

from random import choice

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
        "_cmd_doc_aniq": "<text> - Создать рандомный анимированный стикер",
        "_cmd_doc_aniq1": "<text> - Создать анимированный стикер с рамкой сообщения",
        "_cmd_doc_aniq2": "<text> - Создать анимированный стикер девочки с листочком",
        "_cmd_doc_aniq2": "<text> - Создать анимированный стикер девочки с табличкой",
        "_cmd_doc_aniq2": "<text> - Создать анимированный стикер девочки акулы с рамкой сообщения",
        "_cls_doc": "Простенький модуль, который создает анимированные стикеры",
    }

    async def aniqcmd(self, message: Message):
        """<text> - Create animated quote"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_text"))
            return

        message = await utils.answer(message, self.strings("processing"))

        max_retries = 5
        retry_delay = 5
        success = False

        for _ in range(max_retries):
            try:
                query = await self._client.inline_query("@QuotAfBot", args)
                await message.respond(file=choice(query).document)
                success = True
                break
            except Exception as e:
                await asyncio.sleep(retry_delay)
                continue

        if not success:
            await utils.answer(message, "Failed to fetch animated quote. Please try again later.")

    async def aniq1cmd(self, message: Message):
        """<text> - Create animated quote"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_text"))
            return

        message = await utils.answer(message, self.strings("processing"))

        max_retries = 5
        retry_delay = 5
        success = False

        for _ in range(max_retries):
            try:
                query = await self._client.inline_query("@QuotAfBot", args)
                if query:
                    await message.respond(file=query[0].document)
                    success = True
                    break
            except Exception as e:
                await asyncio.sleep(retry_delay)
                continue

        if not success:
            await utils.answer(message, "Failed to fetch animated quote. Please try again later.")

        if message.out:
            await message.delete()

    async def aniq2cmd(self, message: Message):
        """<text> - Create animated quote"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_text"))
            return

        message = await utils.answer(message, self.strings("processing"))

        max_retries = 5
        retry_delay = 5
        success = False

        for _ in range(max_retries):
            try:
                query = await self._client.inline_query("@QuotAfBot", args)
                if query:
                    await message.respond(file=query[1].document)
                    success = True
                    break
            except Exception as e:
                await asyncio.sleep(retry_delay)
                continue

        if not success:
            await utils.answer(message, "Failed to fetch animated quote. Please try again later.")

        if message.out:
            await message.delete()

    async def aniq3cmd(self, message: Message):
        """<text> - Create animated quote"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_text"))
            return

        message = await utils.answer(message, self.strings("processing"))

        max_retries = 5
        retry_delay = 5
        success = False

        for _ in range(max_retries):
            try:
                query = await self._client.inline_query("@QuotAfBot", args)
                if query:
                    await message.respond(file=query[2].document)
                    success = True
                    break
            except Exception as e:
                await asyncio.sleep(retry_delay)
                continue

        if not success:
            await utils.answer(message, "Failed to fetch animated quote. Please try again later.")

        if message.out:
            await message.delete()


    async def aniq4cmd(self, message: Message):
        """<text> - Create animated quote"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_text"))
            return

        message = await utils.answer(message, self.strings("processing"))

        max_retries = 5
        retry_delay = 5
        success = False

        for _ in range(max_retries):
            try:
                query = await self._client.inline_query("@QuotAfBot", args)
                if query:
                    await message.respond(file=query[3].document)
                    success = True
                    break
            except Exception as e:
                await asyncio.sleep(retry_delay)
                continue

        if not success:
            await utils.answer(message, "Failed to fetch animated quote. Please try again later.")

        if message.out:
            await message.delete()
