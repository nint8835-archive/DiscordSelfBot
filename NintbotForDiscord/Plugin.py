import os

__author__ = 'Riley Flynn (nint8835)'


class BasePlugin:

    def __init__(self, bot_instance: "Bot", plugin_data: dict, folder: os.path):
        self.bot = bot_instance
        self.plugin_data = plugin_data
        self.folder = folder
