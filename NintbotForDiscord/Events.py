from typing import Union

import discord

from NintbotForDiscord.Enums import EventTypes

DiscordUser = Union[discord.User, discord.Member]
DiscordChannel = Union[discord.Channel, discord.PrivateChannel]


class Event(object):

    event_type = EventTypes.GENERIC

    @staticmethod
    def from_dict(args: dict) -> "Event":
        return Event()

    def __getitem__(self, item: str):
        return getattr(self, item)


class MessageSentEvent(Event):

    event_type = EventTypes.MESSAGE_SENT

    def __init__(self, message: discord.Message, author: DiscordUser, channel: DiscordChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: DiscordUser
        self.channel = channel  # type: DiscordChannel
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "MessageSentEvent":
        return MessageSentEvent(args["message"], args["author"], args["channel"])


class ChannelMessageSentEvent(MessageSentEvent):

    event_type = EventTypes.CHANNEL_MESSAGE_SENT

    # noinspection PyMissingConstructor
    def __init__(self, message: discord.Message, author: discord.Member, channel: discord.Channel):
        self.message = message  # type: discord.Message
        self.author = author  # type: discord.Member
        self.channel = channel  # type: discord.Channel
        self.content = message.content  # type: str
        self.server = channel.server  # type: discord.Server

    @staticmethod
    def from_dict(args: dict) -> "ChannelMessageSentEvent":
        return ChannelMessageSentEvent(args["message"], args["author"], args["channel"])


class PrivateMessageSentEvent(MessageSentEvent):

    event_type = EventTypes.PRIVATE_MESSAGE_SENT

    # noinspection PyMissingConstructor
    def __init__(self, message: discord.Message, author: discord.User, channel: discord.PrivateChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: discord.User
        self.channel = channel  # type: discord.PrivateChannel
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "PrivateMessageSentEvent":
        return PrivateMessageSentEvent(args["message"], args["author"], args["channel"])


class MessageDeletedEvent(Event):

    event_type = EventTypes.MESSAGE_DELETED

    def __init__(self, message: discord.Message, author: DiscordUser, channel: DiscordChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: DiscordUser
        self.channel = channel  # type: DiscordChannel
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "MessageDeletedEvent":
        return MessageDeletedEvent(args["message"], args["author"], args["channel"])


class ChannelMessageDeletedEvent(MessageDeletedEvent):

    event_type = EventTypes.CHANNEL_MESSAGE_DELETED

    # noinspection PyMissingConstructor
    def __init__(self, message: discord.Message, author: discord.Member, channel: discord.Channel):
        self.message = message  # type: discord.Message
        self.author = author  # type: discord.Member
        self.channel = channel  # type: discord.Channel
        self.server = channel.server  # type: discord.Server
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "ChannelMessageDeletedEvent":
        return ChannelMessageDeletedEvent(args["message"], args["author"], args["channel"])


class PrivateMessageDeletedEvent(MessageDeletedEvent):

    event_type = EventTypes.PRIVATE_MESSAGE_DELETED

    # noinspection PyMissingConstructor
    def __init__(self, message: discord.Message, author: discord.User, channel: discord.PrivateChannel):
        self.message = message  # type: discord.Message
        self.author = author  # type: discord.User
        self.channel = channel  # type: discord.PrivateChannel
        self.content = message.content  # type: str

    @staticmethod
    def from_dict(args: dict) -> "PrivateMessageDeletedEvent":
        return PrivateMessageDeletedEvent(args["message"], args["author"], args["channel"])

classes = {
    EventTypes.GENERIC: Event,
    EventTypes.MESSAGE_SENT: MessageSentEvent,
    EventTypes.CHANNEL_MESSAGE_SENT: ChannelMessageSentEvent,
    EventTypes.PRIVATE_MESSAGE_SENT: PrivateMessageSentEvent,
    EventTypes.MESSAGE_DELETED: MessageDeletedEvent,
    EventTypes.CHANNEL_MESSAGE_DELETED: ChannelMessageDeletedEvent,
    EventTypes.PRIVATE_MESSAGE_DELETED: PrivateMessageDeletedEvent
}
