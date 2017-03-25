from discord import Member

from .Permission import Permission

__author__ = 'Riley Flynn (nint8835)'


class Owner(Permission):
    def __init__(self, bot_instance):
        self.bot = bot_instance

    def has_permission(self, member: Member) -> bool:
        return member.id == self.bot.config["owner_id"]


# noinspection PyBroadException
class Role(Permission):

    def __init__(self, role_name: str):
        self.role_name = role_name

    def has_permission(self, member: Member) -> bool:

        try:
            return any([role.name == self.role_name for role in member.roles])
        except:
            return False


class Server(Permission):

    def __init__(self, server_id: str):
        self.server_id = server_id

    def has_permission(self, member: Member) -> bool:
        return member.server.id == self.server_id
