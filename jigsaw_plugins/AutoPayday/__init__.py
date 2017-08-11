import asyncio

from discord import Object
from NintbotForDiscord.Plugin import BasePlugin


class AutoPayday(BasePlugin):

    def __init__(self, manifest, bot):
        super().__init__(manifest, bot)

        self.bot.EventManager.loop.create_task(self.payday_task())

    async def payday_task(self):
        while not self.bot.is_closed:
            await asyncio.sleep(200)
            message = await self.bot.send_message(Object("333333334430187520"), "+payday")
            await self.bot.delete_message(message)
