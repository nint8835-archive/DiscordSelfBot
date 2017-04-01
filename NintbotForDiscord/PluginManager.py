import os
from typing import List

import jigsaw
from . import Bot
from .Plugin import BasePlugin

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

    def get_plugin(self, name: str) -> BasePlugin:
        return self._jigsaw.get_plugin(name)

    def get_plugin_manifest(self, name: str) -> dict:
        return self._jigsaw.get_manifest(name)

    def get_all_manifests(self) -> List[dict]:
        manifests = []
        for plugin in self._jigsaw.get_all_plugins():
            manifests.append(plugin["manifest"])

        return manifests
