# meta developer: @Mmazzerratti

from telethon.tl.types import Message
from .. import loader, utils
from random import randint
import asyncio


@loader.tds
class ModuleAnimatedQuotes(loader.Module):
    strings_ru = {
        "name": "Модуль "
                "[AnimatedQuotes]",
        "no_text": (
            "🚫 <b>Укажи текст для создания стикера</b>"
        ),
        "processing": (
            "⌛️ <b>Думаю...</b>"
        ),
        "erroeaq": (
            "<b>Ошибка</b>"
        ),
        "_cmd_doc_aniq": "<index> <text> - Создать рандомный анимированный стикер",
        "_cls_doc": "Модуль, который создает анимированные стикеры",
    }

    strings_en = {
        "name": "Module "
                "[AnimatedQuotes]",
        "no_text": (
            "🚫 <b>Specify the text for creating a sticker</b>"
        ),
        "processing": (
            "⌛️ <b>Think...</b>"
        ),
        "erroeaq": (
            "<b>Error</b>"
        ),
        "_cmd_doc_aniq": "<index> <text> - Create a random animated sticker",
        "_cls_doc": "A module that creates animated stickers",
    }

    async def generatefoto(self, message: Message, image_index: int, args: str):
        if not args:
            await utils.answer(message, self.strings["no_text"])
            return
        processing_message = await utils.answer(message, self.strings["processing"])
        max_retries = 5
        retry_delay = 5
        success = False
        for _ in range(max_retries):
            try:
                query = await self._client.inline_query("@QuotAfBot", args)
                if query and len(query) >= image_index + 1:
                    await processing_message.respond(file=query[image_index].document)
                    success = True
                    break
            except Exception:
                await asyncio.sleep(retry_delay)
                continue
        if not success:
            await utils.answer(message, self.strings["erroeaq"])
        if message.out:
            await message.delete()


    async def aniqcmd(self, message: Message):
        args = utils.get_args_raw(message).strip()
        if args.startswith('1 '):
            image_index = 0
            text = args[2:].strip()
        elif args.startswith('2 '):
            image_index = 1
            text = args[2:].strip()
        elif args.startswith('3 '):
            image_index = 2
            text = args[2:].strip()
        elif args.startswith('4 '):
            image_index = 3
            text = args[2:].strip()
        elif args.startswith('5 '):
            image_index = 4
            text = args[2:].strip()
        elif args.isdigit():
            image_index = int(args)
            text = ""
        else:
            image_index = randint(0, 4)
            text = args
        await self.generatefoto(message, image_index, text)
