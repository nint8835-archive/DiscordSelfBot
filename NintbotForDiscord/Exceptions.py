__author__ = 'Riley Flynn (nint8835)'


class PluginNotFoundException(Exception):
    """An exception raised when something tries to access a plugin that doesn't exist"""
    pass


class MultiplePluginsFoundException(Exception):
    """An exception raised when there are multiple plugins found with a certain name, so it cannot get just one"""
    pass


class CommandNotFoundException(Exception):
    """An exception raised when something attempts to get info for a non-existant command from the CommandRegistry"""
    pass


class MultpleCommandsFoundException(Exception):
    """An exception raised when something tries to get info for one command, but there are multiple commands that match"""
    pass
