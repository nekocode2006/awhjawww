# meta developer: @Mmazzerratti

from telethon.tl.types import Message
from .. import loader, utils
from io import StringIO
import traceback
import sys

@loader.tds
class AnimatedQuotesMod(loader.Module):
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
