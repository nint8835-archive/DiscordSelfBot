from .General import ManageServer, ManageRoles, ManageChannels, KickMembers, BanMembers, CreateInstantInvite, \
    ManageNicknames, ChangeNicknames, Administrator
from .Text import ReadMessages, SendTTSMessages, ManageMessages, EmbedLinks, AttachFiles, ReadMessageHistory, \
    MentionEveryone, SendMessages
from .Voice import Connect, Speak, MuteMembers, DeafenMembers, MoveMembers, UseVoiceActivity
from .Permission import PermissionGroup

__author__ = 'Riley Flynn (nint8835)'


class All(PermissionGroup):
    """A permission group containing all non-custom permissions"""
    permissions = {Administrator(),
                   ManageServer(),
                   ManageRoles(),
                   ManageChannels(),
                   KickMembers(),
                   BanMembers(),
                   CreateInstantInvite(),
                   ReadMessages(),
                   SendMessages(),
                   SendTTSMessages(),
                   ManageMessages(),
                   EmbedLinks(),
                   AttachFiles(),
                   ReadMessageHistory(),
                   MentionEveryone(),
                   Connect(),
                   Speak(),
                   MuteMembers(),
                   DeafenMembers(),
                   MoveMembers(),
                   UseVoiceActivity(),
                   ChangeNicknames(),
                   ManageNicknames()}


class Default(PermissionGroup):
    """A permission group containing permissions granted to the @everyone role on a freshly created Discord server"""
    permissions = [CreateInstantInvite(),
                   ReadMessages(),
                   SendMessages(),
                   SendTTSMessages(),
                   EmbedLinks(),
                   AttachFiles(),
                   ReadMessageHistory(),
                   MentionEveryone(),
                   Connect(),
                   Speak(),
                   UseVoiceActivity()]
