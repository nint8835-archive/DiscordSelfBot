import jigsaw
from NintbotForDiscord import Bot

__author__ = 'Riley Flynn (nint8835)'


class PluginManager:

    def __init__(self, bot):
        self.bot = bot  # type: Bot.Bot
        self._jigsaw = jigsaw.PluginLoader()

    def load_plugins(self):
        self._jigsaw.load_manifests()
        self._jigsaw.load_plugins(self.bot)
