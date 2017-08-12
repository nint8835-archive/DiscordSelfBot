from pyfiglet import Figlet

from NintbotForDiscord.Events import CommandSentEvent
from jigsaw_plugins.UserCore import UserCorePlugin


class FancyText(UserCorePlugin):
    def __init__(self, manifest, bot_instance):
        super().__init__(manifest, bot_instance)

        self.register_modern_command("^fancy ([^~]+)$", "Prints text in a fancy way", self.command_fancy)
        self.register_modern_command("^fancy ([\\S ]+) ~([\\S]+)$", "Prints text in a fancy way with a custom font", self.command_customfancy)
        self.figlet = Figlet()

    async def command_fancy(self, args: CommandSentEvent):
        text = args.args
        processed_text = self.figlet.renderText(text)

        await self.bot.send_message(args.channel, f"```\n{processed_text}```")

    async def command_customfancy(self, args: CommandSentEvent):
        text = args.args[0]
        font = args.args[1]
        figlet = Figlet(font)
        processed_text = figlet.renderText(text)

        await self.bot.send_message(args.channel, f"```\n{processed_text}```")
