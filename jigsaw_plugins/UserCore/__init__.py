from NintbotForDiscord.Permissions.Special import Owner
from plugins.JigsawLoader import NintbotPlugin


class UserCorePlugin(NintbotPlugin):

    def __init__(self, manifest, bot_instance):
        super().__init__(manifest, bot_instance)

        self._internal_handlers = {}

    async def command_handler(self, args: dict):
        await self._internal_handlers[args["command_args"][0]](args)

        await self.bot.delete_message(args["message"])

    def register_user_command(self, name: str, description: str, method: classmethod, *args, **kwargs):
        self._internal_handlers[name] = method
        NintbotPlugin.register_command(self, name, description, method, Owner(self.bot))

    def register_command(self, *args, **kwargs):
        self.register_user_command(*args, **kwargs)


class UserCore(NintbotPlugin):
    def enable(self) -> None:
        super().enable()
        self.logger.debug(f"UserCore v{self.manifest.get('version', 'UNKNOWN')} available for use.")
