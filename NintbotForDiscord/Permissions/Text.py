from discord import Member
from .Permission import Permission

__author__ = 'Riley Flynn (nint8835)'


# noinspection PyBroadException
class ReadMessages(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.read_messages for role in member.roles])
        except:
            return True


# noinspection PyBroadException
class SendMessages(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.send_messages for role in member.roles])
        except:
            return True


# noinspection PyBroadException
class SendTTSMessages(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.send_tts_messages for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class ManageMessages(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.manage_messages for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class EmbedLinks(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.embed_links for role in member.roles])
        except:
            return True


# noinspection PyBroadException
class AttachFiles(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.attach_files for role in member.roles])
        except:
            return True


# noinspection PyBroadException
class ReadMessageHistory(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.read_message_history for role in member.roles])
        except:
            return True


# noinspection PyBroadException
class MentionEveryone(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.mention_everyone for role in member.roles])
        except:
            return False


# noinspection PyBroadException
class UseExternalEmojis(Permission):

    def has_permission(self, member: Member) -> bool:
        try:
            return any([role.permissions.external_emojis for role in member.roles])
        except:
            return True
