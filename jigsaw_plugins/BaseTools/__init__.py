import contextlib
import datetime
import sys
import traceback
from io import StringIO

from discord import Colour, Embed, Game

from NintbotForDiscord.Events import CommandSentEvent
from jigsaw_plugins.UserCore import UserCorePlugin


@contextlib.contextmanager
def stdioreader():
    old = (sys.stdout, sys.stderr)
    stdout = StringIO()
    stderr = StringIO()
    sys.stdout = stdout
    sys.stderr = stderr
    yield stdout, stderr
    sys.stdout = old[0]
    sys.stderr = old[1]


class BaseTools(UserCorePlugin):

    def __init__(self, manifest, bot_instance):
        super().__init__(manifest, bot_instance)

        self.register_user_command("eval", "Evaluates given code", self.command_eval)
        self.register_user_command("exec", "Executes given code", self.command_exec)
        self.register_user_command("setgame", "Sets the currently played code", self.command_setgame)
        self.register_modern_command("^ping$", "Tests the response time for command handling", self.command_ping)

    async def command_eval(self, args: dict):
        code = args["content"].split(self.bot.config["command_prefix"]+"eval ")[1]
        try:
            result = str(eval(code))
            colour = Colour.green()
        except:
            result = f"```py\n{traceback.format_exc(1)}```"
            colour = Colour.red()

        result.replace("\\", "\\\\")

        embed = Embed()
        embed.add_field(name=code, value=result)
        embed.colour = colour

        await self.bot.send_message(args["channel"], embed=embed)

    async def command_exec(self, args: dict):
        code = args["content"].split(self.bot.config["command_prefix"]+"exec ")[1]
        with stdioreader() as (out, err):  # type: StringIO
            try:
                exec(code)
                result = out.getvalue()
                colour = Colour.green()
            except:
                result = f"```py\n{traceback.format_exc(1)}```"
                colour = Colour.red()

        result.replace("\\", "\\\\")

        embed = Embed()
        embed.add_field(name=code, value=result)
        embed.colour = colour

        await self.bot.send_message(args["channel"], embed=embed)

    async def command_setgame(self, args: dict):
        game = args["unsplit_args"].split("setgame ")[1]
        await self.bot.change_presence(game=Game(name=game))

    async def command_ping(self, args: CommandSentEvent):
        time_diff = datetime.datetime.utcnow().timestamp() - args.message.timestamp.timestamp()

        await self.bot.send_message(args.channel, f"Pong! I processed this command {time_diff} seconds after it was sent!")
