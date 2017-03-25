import logging

from NintbotForDiscord import Bot
from NintbotForDiscord.Enums import EventTypes
from NintbotForDiscord.Permissions import Permission
from jigsaw import JigsawPlugin

__author__ = 'Riley Flynn (nint8835)'


class BasePlugin(JigsawPlugin):

    def __init__(self, manifest, bot_instance):
        super(BasePlugin, self).__init__(manifest)

        self.bot = bot_instance  # type: Bot.Bot

        self._registered_commands = []
        self._registered_handlers = []

        self.logger = logging.getLogger(self.manifest["name"])

    def register_command(self, name: str, description: str, method: classmethod, permission: Permission = Permission()) -> None:
        """
        Adds a command to the internal command registry to be auto-registered/unregistered on enable/disable
        :param name: The command name
        :param description: The command description
        :param method: The method that will handle the command
        :param permission: The permission required to use the command
        """
        self._registered_commands.append({
            "command": name,
            "description": description,
            "required_perm": permission,
            "plugin": self,
            "command_handler": method
        })

    def register_handler(self, event_type: EventTypes, event_handler: classmethod) -> None:
        """
        Adds a handler to the internal handler registry to be auto-registered/unregistered on enable/disable
        :param event_type: The type of event this handler will handle
        :param event_handler: The method that will handle the event
        """
        self._registered_handlers.append({
            "event_type": event_type,
            "event_handler": event_handler,
            "plugin": self
        })

    def enable(self) -> None:
        self.logger.debug("Registering commands...")
        for command in self._registered_commands:
            self.bot.CommandRegistry.register_command(**command)
        self.logger.debug("Commands registered.")

        self.logger.debug("Registering handlers...")
        for handler in self._registered_handlers:
            self.bot.EventManager.register_handler(**handler)
        self.logger.debug("Handlers registered.")

    def disable(self) -> None:
        self.logger.debug("Unregistering commands...")
        self.bot.CommandRegistry.unregister_all_commands_for_plugin(self)
        self.logger.debug("Commands unregistered.")

        self.logger.debug("Unregistering handlers...")
        self.bot.EventManager.remove_handlers(self)
