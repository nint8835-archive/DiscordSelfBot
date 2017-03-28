from NintbotForDiscord.Permissions.Special import Owner
from NintbotForDiscord.Plugin import BasePlugin


class UserCorePlugin(BasePlugin):

    def __init__(self, manifest, bot_instance):
        super().__init__(manifest, bot_instance)

        self._internal_handlers = {}

    async def command_handler(self, args: dict):
        await self._internal_handlers[args["command_args"][0]](args)

        await self.bot.delete_message(args["message"])

    def register_user_command(self, name: str, description: str, method: classmethod, *args, **kwargs):
        self._internal_handlers[name] = method
        BasePlugin.register_command(self, name, description, self.command_handler, Owner(self.bot))

    def register_command(self, *args, **kwargs):
        self.register_user_command(*args, **kwargs)


class UserCore(BasePlugin):
    def enable(self) -> None:
        super().enable()
        self.logger.debug(f"UserCore v{self.manifest.get('version', 'UNKNOWN')} available for use.")
