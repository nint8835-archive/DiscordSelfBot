import io
import json
import os

from .Bot import Bot

__author__ = 'Riley Flynn (nint8835)'


class BotLauncher:

    def __init__(self):
        self.config = self._get_config()
        self._bot = Bot(self.config)

    def _get_config(self) -> dict:
        """
        Returns the config
        :return: The config (in this case an empty dict)
        """
        return {}


class StreamBotLauncher(BotLauncher):

    def __init__(self, f: io.TextIOWrapper):
        self._stream = f
        super(StreamBotLauncher, self).__init__()

    def _get_config(self) -> dict:
        """
        Returns the config
        :return: The config (in this case a dictionary loaded from a I/O stream
        """
        return json.load(self._stream)


class FileBotLauncher(StreamBotLauncher):

    def __init__(self, path: str):
        if os.path.exists(path):
            with open(path) as f:
                super(FileBotLauncher, self).__init__(f)
