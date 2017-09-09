from typing import Union, Tuple

import discord

from .Enums import EventTypes
from .Types import DiscordUser, DiscordTextChannel, DiscordPrivateTextChannel


class Event(object):

    event_type = EventTypes.GENERIC

    @staticmethod
    def from_dict(args: dict) -> "Event":
        return Event()

    def __getitem__(self, item: str):
        return getattr(self, item)


class MessageSentEvent(Event):

    event_type = EventTypes.MESSAGE_SENT

    def __init__(self, message: discord.Message, author: DiscordUser, channel: DiscordTextChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: DiscordUser
        self.channel = channel  # type: DiscordTextChannel
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "MessageSentEvent":
        return MessageSentEvent(args["message"], args["author"], args["channel"])


class ChannelMessageSentEvent(MessageSentEvent):

    event_type = EventTypes.CHANNEL_MESSAGE_SENT

    # noinspection PyMissingConstructor
    def __init__(self, message: discord.Message, author: discord.Member, channel: discord.TextChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: discord.Member
        self.channel = channel  # type: discord.TextChannel
        self.content = message.content  # type: str
        self.server = channel.guild  # type: discord.Guild

    @staticmethod
    def from_dict(args: dict) -> "ChannelMessageSentEvent":
        return ChannelMessageSentEvent(args["message"], args["author"], args["channel"])


class PrivateMessageSentEvent(MessageSentEvent):

    event_type = EventTypes.PRIVATE_MESSAGE_SENT

    # noinspection PyMissingConstructor
    def __init__(self, message: discord.Message, author: discord.User, channel: DiscordPrivateTextChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: discord.User
        self.channel = channel  # type: DiscordPrivateTextChannel
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "PrivateMessageSentEvent":
        return PrivateMessageSentEvent(args["message"], args["author"], args["channel"])


class MessageDeletedEvent(Event):

    event_type = EventTypes.MESSAGE_DELETED

    def __init__(self, message: discord.Message, author: DiscordUser, channel: DiscordTextChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: DiscordUser
        self.channel = channel  # type: DiscordTextChannel
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "MessageDeletedEvent":
        return MessageDeletedEvent(args["message"], args["author"], args["channel"])


class ChannelMessageDeletedEvent(MessageDeletedEvent):

    event_type = EventTypes.CHANNEL_MESSAGE_DELETED

    # noinspection PyMissingConstructor
    def __init__(self, message: discord.Message, author: discord.Member, channel: discord.TextChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: discord.Member
        self.channel = channel  # type: discord.TextChannel
        self.server = channel.guild  # type: discord.Guild
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "ChannelMessageDeletedEvent":
        return ChannelMessageDeletedEvent(args["message"], args["author"], args["channel"])


class PrivateMessageDeletedEvent(MessageDeletedEvent):

    event_type = EventTypes.PRIVATE_MESSAGE_DELETED

    # noinspection PyMissingConstructor
    def __init__(self, message: discord.Message, author: discord.User, channel: DiscordPrivateTextChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: discord.User
        self.channel = channel  # type: DiscordPrivateTextChannel
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "PrivateMessageDeletedEvent":
        return PrivateMessageDeletedEvent(args["message"], args["author"], args["channel"])


class MessageEditedEvent(Event):

    event_type = EventTypes.MESSAGE_EDITED

    def __init__(self, before: discord.Message, after: discord.Message, author: DiscordUser, channel: DiscordTextChannel):
        self.before = before  # type: discord.Message
        self.after = after  # type: discord.Message
        self.author = author  # type: DiscordUser
        self.channel = channel  # type: DiscordTextChannel
        self.content_before = before.content  # type: str
        self.content_after = after.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "MessageEditedEvent":
        return MessageEditedEvent(args["message_before"], args["message_after"], args["author"], args["channel"])


class ChannelMessageEditedEvent(MessageEditedEvent):

    event_type = EventTypes.CHANNEL_MESSAGE_EDITED

    # noinspection PyMissingConstructor
    def __init__(self, before: discord.Message, after: discord.Message, author: discord.Member, channel: discord.TextChannel):
        self.before = before  # type: discord.Message
        self.after = after  # type: discord.Message
        self.author = author  # type: discord.Member
        self.channel = channel  # type: discord.TextChannel
        self.content_before = before.content  # type: str
        self.content_after = after.content  # type: str
        self.server = channel.guild  # type: discord.Guild

    @staticmethod
    def from_dict(args: dict) -> "ChannelMessageEditedEvent":
        return ChannelMessageEditedEvent(args["message_before"], args["message_after"], args["author"], args["channel"])


class PrivateMessageEditedEvent(MessageEditedEvent):

    event_type = EventTypes.PRIVATE_MESSAGE_EDITED

    # noinspection PyMissingConstructor
    def __init__(self, before: discord.Message, after: discord.Message, author: discord.User, channel: DiscordPrivateTextChannel):
        self.before = before  # type: discord.Message
        self.after = after  # type: discord.Message
        self.author = author  # type: discord.User
        self.channel = channel  # type: DiscordPrivateTextChannel
        self.content_before = before.content  # type: str
        self.content_after = after.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "PrivateMessageEditedEvent":
        return PrivateMessageEditedEvent(args["message_before"], args["message_after"], args["author"], args["channel"])


class CommandSentEvent(Event):

    event_type = EventTypes.COMMAND_SENT

    def __init__(self, message: discord.Message, author: DiscordUser, channel: DiscordTextChannel, command: str, args: Tuple[str, ...]):
        self.message = message  # type: discord.Message
        self.author = author  # type: DiscordUser
        self.channel = channel  # type: DiscordTextChannel
        self.content = message.content  # type: str
        self.command = command  # type: str
        self.args = args  # type: Tuple[str, ...]
        self.command_args = self.args

    @staticmethod
    def from_dict(args: dict) -> "CommandSentEvent":
        return CommandSentEvent(args["message"], args["author"], args["channel"], args["command_args"][0], args["command_args"])


# Conversion table for converting dict events to objects
classes = {
    EventTypes.GENERIC: Event,
    EventTypes.MESSAGE_SENT: MessageSentEvent,
    EventTypes.CHANNEL_MESSAGE_SENT: ChannelMessageSentEvent,
    EventTypes.PRIVATE_MESSAGE_SENT: PrivateMessageSentEvent,
    EventTypes.MESSAGE_DELETED: MessageDeletedEvent,
    EventTypes.CHANNEL_MESSAGE_DELETED: ChannelMessageDeletedEvent,
    EventTypes.PRIVATE_MESSAGE_DELETED: PrivateMessageDeletedEvent,
    EventTypes.MESSAGE_EDITED: MessageEditedEvent,
    EventTypes.CHANNEL_MESSAGE_EDITED: ChannelMessageEditedEvent,
    EventTypes.PRIVATE_MESSAGE_EDITED: PrivateMessageEditedEvent,
    EventTypes.COMMAND_SENT: CommandSentEvent
}
