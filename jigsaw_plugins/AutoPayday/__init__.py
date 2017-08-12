import asyncio

from discord import Object
from jigsaw_plugins.UserCore import UserCorePlugin
from NintbotForDiscord.Events import CommandSentEvent


class AutoPayday(UserCorePlugin):

    def __init__(self, manifest, bot):
        super().__init__(manifest, bot)

        self.bot.EventManager.loop.create_task(self.payday_task())

        self.register_modern_command("^slot ([1-9]\d*) ([1-9]\d*)$", "Uses the slot command a specified number of times", self.command_slot)

    async def payday_task(self):
        while not self.bot.is_closed:
            await asyncio.sleep(200)
            message = await self.bot.send_message(Object("333333334430187520"), "+payday")
            await self.bot.delete_message(message)

    async def command_slot(self, args: CommandSentEvent):
        messages = []
        for i in range(int(args.args[0])):
            messages.append(await self.bot.send_message(Object("333333334430187520"), f"+slot {args.args[1]}"))
            await asyncio.sleep(2)

        for message in messages:
            await self.bot.delete_message(message)
            await asyncio.sleep(2)
