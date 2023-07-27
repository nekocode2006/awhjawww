from telethon.tl.types import Message

from .. import loader, utils

@loader.tds
class MusicDLMod(loader.Module):
    strings = {
        "name": "MusicDL",
        "args": "🚫 <b>You forgot to write the name of the song</b>",
        "loading": "🔍 <b>Loading...</b>",
        "404": "🚫 <b>Music </b><code>{}</code><b> not found</b>",
    }

    strings_ru = {
        "args": "🚫 <b>Ты забыл написать название песни</b>",
        "loading": "🔍 <b>Загрузка...</b>",
        "404": "🚫 <b>Песня </b><code>{}</code><b> не найдена</b>",
    }

    async def client_ready(self, *_):
        self.musicdl = await self.import_lib(
            "https://libs.hikariatama.ru/musicdl.py",
            suspend_on_error=True,
        )

    @loader.command(ru_doc="<название> - Скачать песню")
    async def mdl(self, message: Message):
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("args"))
            return

        message = await utils.answer(message, self.strings("loading"))
        result = await self.musicdl.dl(args, only_document=True)

        if not result:
            await utils.answer(message, self.strings("404").format(args))
            return

        await self._client.send_file(
            message.peer_id,
            result,
            caption=f"🎧 Вот это я понимаю трек",
            reply_to=getattr(message, "reply_to_msg_id", None),
        )
        if message.out:
            await message.delete()
