import contextlib
import sys
import traceback
from io import StringIO

from discord import Colour, Embed, Game

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

    async def command_eval(self, args: dict):
        code = args["unsplit_args"].split("eval ")[1]
        try:
            result = eval(code)
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
        code = args["unsplit_args"].split("exec ")[1]
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
