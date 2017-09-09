import discord

from .Types import DiscordChannel


def channel_is_private(channel: DiscordChannel) -> bool:
    return isinstance(channel, discord.abc.PrivateChannel)
