from discord import Member
from .Permission import Permission

__author__ = 'Riley Flynn (nint8835)'


# noinspection PyBroadException
class Connect(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.manage_server for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class Speak(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.speak for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class MuteMembers(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.mute_members for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class DeafenMembers(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.deafen_members for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class MoveMembers(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.move_members for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class UseVoiceActivity(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.use_voice_activity for role in member.roles])
        except:
            return False
