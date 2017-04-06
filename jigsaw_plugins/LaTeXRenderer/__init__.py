import os

from sympy import preview

from NintbotForDiscord.Events import CommandSentEvent
from jigsaw_plugins.UserCore import UserCorePlugin


class LaTeXRenderer(UserCorePlugin):
    def __init__(self, manifest, bot_instance):
        super().__init__(manifest, bot_instance)
        self.register_user_command("latex", "Renders a latex expression", self.command_latex)

    async def command_latex(self, event: CommandSentEvent):
        expression = event.content.split(self.bot.config["command_prefix"] + "latex ")[1]
        preview(expression, euler=False, viewer="file", filename=os.path.join(self.manifest["path"], "latex.png"), packages=("color", ))
        await self.bot.send_file(event.channel, os.path.join(self.manifest["path"], "latex.png"))
