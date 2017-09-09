from typing import Union

import discord


DiscordUser = Union[discord.User, discord.Member]
DiscordTextChannel = Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel]
DiscordPrivateTextChannel = Union[discord.DMChannel, discord.GroupChannel]
DiscordGuildChannel = Union[discord.TextChannel, discord.VoiceChannel]
DiscordChannel = Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel, discord.VoiceChannel]
