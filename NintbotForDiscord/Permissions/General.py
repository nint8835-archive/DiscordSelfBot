from discord import Member
from .Permission import Permission

__author__ = 'Riley Flynn (nint8835)'


# noinspection PyBroadException
class Administrator(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.administrator for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class ManageServer(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.manage_server for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class ManageRoles(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.manage_roles for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class ManageChannels(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.manage_channels for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class KickMembers(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.kick_members for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class BanMembers(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.ban_members for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class CreateInstantInvite(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.create_instant_invite for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class ChangeNicknames(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.change_nicknames for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class ManageNicknames(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.manage_nicknames for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class ManageEmojis(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.manage_emojis for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class ManageWebhooks(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.manage_webhooks for role in member.roles])
        except:
            return False
