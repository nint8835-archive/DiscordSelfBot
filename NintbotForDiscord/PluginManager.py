import os

import jigsaw
from NintbotForDiscord import Bot

__author__ = 'Riley Flynn (nint8835)'


class PluginManager:

    def __init__(self, bot):
        self.bot = bot  # type: Bot.Bot
        self._jigsaw = jigsaw.PluginLoader(plugin_paths=(
            os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "plugins")),
            os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "jigsaw_plugins"))
        ))

    def load_plugins(self):
        self._jigsaw.load_manifests()
        self._jigsaw.load_plugins(self.bot)
        self._jigsaw.enable_all_plugins()
