import asyncio
import logging

import discord

from NintbotForDiscord.Plugin import BasePlugin
from .Permissions import Permission
from .Exceptions import CommandNotFoundException, MultpleCommandsFoundException

__author__ = 'Riley Flynn (nint8835)'


class CommandRegistry:

    def __init__(self, bot):
        self._commands = []
        self.logger = logging.getLogger("CommandRegistry")
        self.bot = bot

    def register_command(self, command: str, description: str, required_perm: Permission, plugin: BasePlugin, command_handler: classmethod = None):
        """
        Adds a command to the command registry
        :param command: The command
        :param description: The command description
        :param required_perm: The permission required to run the command
        :param plugin: The plugin instance
        :param command_handler: A coroutine that will handle the command
        """
        self._commands.append({
            "command": command,
            "description": description,
            "required_permission": required_perm,
            "plugin": plugin,
            "handler": command_handler
        })
        self.logger.debug("New command registered. Info: {}".format(self._commands[-1]))

    def unregister_command(self, command_name: str, plugin: BasePlugin):
        """
        Removes a command from the command registry
        :param command_name: The name of the command to unregister
        :param plugin: The plugin that registered it
        """
        for command in self._commands[:]:
            if command["command"] == command_name and command["plugin"] == plugin:
                self._commands.remove(command)

    def unregister_all_commands_for_plugin(self, plugin: BasePlugin):
        """
        Removes all commands for a plugin from the command registry
        :param plugin: The plugin to remove all commands from
        """
        for command in self._commands[:]:
            if command["plugin"] == plugin:
                self._commands.remove(command)

    def get_available_commands_for_user(self, user: discord.User) -> list:
        """
        Returns all commands a user has access to
        :param user: The user to return accessible commands for
        :return: A list of commands the user has access to
        """
        return [i for i in self._commands if i["required_permission"].has_permission(user)]

    def get_info_for_command(self, command: str) -> list:
        """
        Returns a list of all commands with specified command
        :param command: The command to return all results for
        :return: The list of results for that command
        """
        return [i for i in self._commands if i["command"] == command]

    async def handle_command(self, command_name: str, args: dict):
        """
        Checks for a command in the command registry, and then runs it
        :param command_name: The command to run
        :param args: The argument dictionary to pass to the handler
        """
        self.logger.debug("Handling command {}.".format(command_name))
        for command in self._commands:
            if command["command"] == command_name:
                if command["handler"] is not None:
                    if command["required_permission"].has_permission(args["author"]):
                        try:
                            await asyncio.wait_for(command["handler"](args),
                                                   timeout=self.bot.config["event_timeout"],
                                                   loop=self.bot.EventManager.loop)
                        except asyncio.TimeoutError:
                            self.bot.logger.warning("Handling of {} command from plugin {} timed out.".format(command,
                                                                                                              command["plugin"].manifest["name"]))
