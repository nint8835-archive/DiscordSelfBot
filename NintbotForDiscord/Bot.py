import datetime
import discord
import asyncio
import shlex
import logging

from .Plugin import BasePlugin
from .EventManager import EventManager
from .PluginManager import PluginManager
from .Enums import EventTypes
from .CommandRegistry import CommandRegistry
from .Scheduler import Scheduler
from . import __version__

__author__ = 'Riley Flynn (nint8835)'


class Bot(discord.Client):
    def __init__(self, config: dict, loop: asyncio.BaseEventLoop = None):
        """
        Initializes a new NintbotForDiscord instance
        :param config: A dictionary object containing the bot's settings
        :param loop: The asyncio event loop to handle connection to Discord
        """
        super(Bot, self).__init__(loop=loop)
        self.VERSION = __version__
        self.config = config
        self.logger = logging.getLogger("NintbotForDiscord")

        try:
            log_level = getattr(logging, self.config["log_level"])
        except AttributeError:
            log_level = logging.INFO

        logging.basicConfig(format="{%(asctime)s} (%(name)s) [%(levelname)s]: %(message)s",
                            datefmt="%x, %X",
                            level=log_level)
        self.logger.debug("Creating EventManager...")
        self.EventManager = EventManager(self)
        self.logger.debug("Done.")
        self.logger.debug("Creating PluginManager...")
        self.PluginManager = PluginManager(self)
        self.logger.debug("Done.")
        self.logger.debug("Creating CommandRegistry...")
        self.CommandRegistry = CommandRegistry(self)
        self.logger.debug("Done")
        self.logger.debug("Creating Scheduled...")
        self.Scheduler = Scheduler(self)
        self.logger.debug("Done")
        self.logger.debug("Loading plugins...")
        self.PluginManager.load_plugins()
        self.logger.debug("Done.")
        self.logger.debug("Starting bot...")
        logging.getLogger("discord").setLevel(logging.ERROR)
        logging.getLogger("websockets").setLevel(logging.ERROR)
        self.email = self.config["email"]
        self.run(config["token"], bot=self.config["bot"])

    def register_handler(self, eventtype: EventTypes, handler, plugin: BasePlugin):
        """
        Registers a new event handler in the bot's EventManager
        :param eventtype: The type of event for the handler to handle
        :param handler: The coroutine that will handle the event
        :param plugin: The instance of the plugin that will handle the event
        """
        self.EventManager.register_handler(eventtype, handler, plugin)

    async def on_message(self, message: discord.Message):
        """
        Passes incoming messages to the EventManager
        :param message: The incoming message
        """
        if message.channel.is_private or message.server.id not in self.config.get("blacklisted_servers", []):
            await self.log_message(message)
            await self.EventManager.dispatch_event(EventTypes.MESSAGE_SENT,
                                                   message=message,
                                                   author=message.author,
                                                   channel=message.channel)
            if message.channel.is_private:
                await self.EventManager.dispatch_event(EventTypes.PRIVATE_MESSAGE_SENT,
                                                       message=message,
                                                       author=message.author,
                                                       channel=message.channel)
            else:
                await self.EventManager.dispatch_event(EventTypes.CHANNEL_MESSAGE_SENT,
                                                       message=message,
                                                       author=message.author,
                                                       channel=message.channel)

            if message.content.startswith(self.config["command_prefix"]):
                command_str = message.content.lstrip(self.config["command_prefix"])
                try:
                    args = shlex.split(command_str)
                except ValueError:
                    self.logger.warning("Failed to process arguments for message '{}' using shlex, falling back to\
                                         processing using spaces.".format(message.content))
                    args = command_str.split(" ")
                await self.EventManager.dispatch_event(EventTypes.COMMAND_SENT,
                                                       command_args=args,
                                                       unsplit_args=command_str,
                                                       message=message,
                                                       author=message.author,
                                                       channel=message.channel)

    async def on_message_delete(self, message: discord.Message):
        """
        Passes message deletions to the EventManager
        :param message: The message that was deleted
        """
        if message.channel.is_private or message.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MESSAGE_DELETED,
                                                   message=message,
                                                   author=message.author,
                                                   channel=message.channel)

            if message.channel.is_private:
                await self.EventManager.dispatch_event(EventTypes.PRIVATE_MESSAGE_DELETED,
                                                       message=message,
                                                       author=message.author,
                                                       channel=message.channel)

            else:
                await self.EventManager.dispatch_event(EventTypes.CHANNEL_MESSAGE_DELETED,
                                                       message=message,
                                                       author=message.author,
                                                       channel=message.channel)

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        """
        Passes message edits to the EventManager
        :param before: The message before it was edited
        :param after: The message after it was edited
        """
        if after.channel.is_private or after.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MESSAGE_EDITED,
                                                   message_before=before,
                                                   message_after=after,
                                                   author=after.author,
                                                   channel=after.channel)

            if after.channel.is_private:
                await self.EventManager.dispatch_event(EventTypes.PRIVATE_MESSAGE_EDITED,
                                                       message_before=before,
                                                       message_after=after,
                                                       author=after.author,
                                                       channel=after.channel)

            else:
                await self.EventManager.dispatch_event(EventTypes.PRIVATE_MESSAGE_EDITED,
                                                       message_before=before,
                                                       message_after=after,
                                                       author=after.author,
                                                       channel=after.channel)

    async def on_channel_delete(self, channel: discord.Channel):
        """
        Passes channel deletions to the EventManager
        :param channel: The channel that was deleted
        """
        if channel.is_private or channel.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.CHANNEL_DELETED,
                                                   channel=channel,
                                                   server=channel.server)

    async def on_channel_create(self, channel: discord.Channel):
        """
        Passes channel creations to the EventManager
        :param channel: The channel that was created
        """
        if channel.is_private or channel.server.id not in self.config.get("blacklisted_servers", []):
            if not channel.is_private:
                await self.EventManager.dispatch_event(EventTypes.CHANNEL_CREATED,
                                                       channel=channel,
                                                       server=channel.server)
            else:
                await self.EventManager.dispatch_event(EventTypes.CHANNEL_CREATED,
                                                       channel=channel)

    async def on_channel_update(self, before: discord.Channel, after: discord.Channel):
        """
        Passes channel updates to the EventManager
        :param before: The channel before it was updated
        :param after: The channel after it was updated
        """
        if after.is_private or after.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.CHANNEL_UPDATED,
                                                   channel_before=before,
                                                   channel_after=after,
                                                   server=after.server)

    async def on_member_join(self, member: discord.Member):
        """
        Passes member joins to the EventManager
        :param member: The member that joined
        """
        if member.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MEMBER_JOINED,
                                                   member=member,
                                                   server=member.server)

    async def on_member_remove(self, member: discord.Member):
        """
        Passes member leaves to the EventManager
        :param member: The member that left
        """
        if member.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MEMBER_LEFT,
                                                   member=member,
                                                   server=member.server)

    async def on_member_update(self, before: discord.Member, after: discord.Member):
        """
        Passes member updates to the EventManager
        :param before: The member before the update
        :param after: The member after the update
        """
        if after.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MEMBER_UPDATED,
                                                   member_before=before,
                                                   member_after=after,
                                                   server=after.server)

    async def on_member_ban(self, member: discord.Member):
        """
        Passes member bans to the EventManager
        :param member: The member that was banned
        """
        if member.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MEMBER_BANNED,
                                                   member=member,
                                                   server=member.server)

    async def on_member_unban(self, server: discord.Server, user: discord.User):
        """
        Passes member unbans to the EventManager
        :param server: The server that the user was unbanned from
        :param user: The user that was unbanned
        """
        if server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MEMBER_UNBANNED,
                                                   server=server,
                                                   user=user)

    async def on_voice_state_update(self, before: discord.Member, after: discord.Member):
        """
        Passes voice state updates to the EventManager
        :param before: The member before the update
        :param after: The member after the update
        """
        if after.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MEMBER_VOICE_STATE_UPDATED,
                                                   member_before=before,
                                                   member_after=after)

    async def on_typing(self, channel: discord.Channel, user: discord.User, when: datetime.datetime):
        """
        Passes typing notifications to the EventManager
        :param channel: The channel that the user is typing in
        :param user: The user that is typing
        :param when: When the user started typing
        """
        if channel.is_private or channel.server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.MEMBER_TYPING,
                                                   channel=channel,
                                                   user=user,
                                                   when=when)

    async def on_server_join(self, server: discord.Server):
        """
        Passes server joins to the EventManager
        :param server: The server that was joined
        """
        if server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.SERVER_JOINED,
                                                   server=server)

    async def on_server_remove(self, server: discord.Server):
        """
        Passes server leaves to the EventManager
        :param server: The server that was left
        """
        if server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.SERVER_LEFT,
                                                   server=server)

    async def on_server_update(self, before: discord.Server, after: discord.Server):
        """
        Passes server updates to the EventManager
        :param before: The server before the update
        :param after: The server after the update
        """
        if before.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.SERVER_UPDATED,
                                                   server_before=before,
                                                   server_after=after)

    async def on_server_available(self, server: discord.Server):
        """
        Passes server available events to the EventManager
        :param server: The server that became available
        """
        if server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.SERVER_AVAILABLE,
                                                   server=server)

    async def on_server_unavailable(self, server: discord.Server):
        """
        Passes server unavailable events to the EventManager
        :param server: The server that became unavailable
        """
        if server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.SERVER_UNAVAILABLE,
                                                   server=server)

    async def on_server_role_create(self, server: discord.Server, role: discord.Role):
        """
        Passes server role creations to the EventManager
        :param server: The server that the role was created in
        :param role: The role that was created
        """
        if server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.SERVER_ROLE_CREATED,
                                                   server=server,
                                                   role=role)

    async def on_server_role_delete(self, server: discord.Server, role: discord.Role):
        """
        Passes server role deletions to the EventManager
        :param server: The server that the role was deleted from
        :param role: The role that was deleted
        """
        if server.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.SERVER_ROLE_DELETED,
                                                   server=server,
                                                   role=role)

    async def on_server_role_update(self, before: discord.Role, after: discord.Role):
        """
        Passes server role updates to the EventManager
        :param before: The role before the update
        :param after: The role after the update
        """
        if before.id not in self.config.get("blacklisted_servers", []):
            await self.EventManager.dispatch_event(EventTypes.SERVER_ROLE_UPDATED,
                                                   role_before=before,
                                                   role_after=after,
                                                   server=[server for server in self.servers if after in server.roles][0])

    async def on_ready(self):
        """
        Passes ready events to the EventManager
        """
        await self.EventManager.dispatch_event(EventTypes.CLIENT_READY)

    async def log_message(self, message: discord.Message):
        """
        Logs incoming messages to the console
        :param message: The message to log
        """
        self.logger.info("{} ({}) -> ({}): {}".format(message.author.name,
                                                      message.author.id,
                                                      message.channel.id,
                                                      message.content))
