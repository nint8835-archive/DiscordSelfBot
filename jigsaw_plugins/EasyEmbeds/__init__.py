import json

from discord import Embed, Colour

from jigsaw_plugins.UserCore import UserCorePlugin


class EasyEmbeds(UserCorePlugin):

    def __init__(self, manifest, bot_instance):
        super().__init__(manifest, bot_instance)

        self.register_user_command("jsonembed", "Creates an embed out of a json object", self.command_jsonembed)

    async def command_jsonembed(self, args: dict):
        obj = json.loads(args.content.split("jsonembed ")[1])

        embed = Embed()

        for key in obj:
            if key == "colour":
                continue
            embed.add_field(name=key, value=obj[key])

        embed.colour = Colour(int(obj.get("colour", "673AB7"), 16))

        await args["channel"].send(embed=embed)
