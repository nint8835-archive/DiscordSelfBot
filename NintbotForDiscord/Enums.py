from enum import Enum
__author__ = 'Riley Flynn (nint8835)'


class EventTypes(Enum):
    """An enum containing all of the event types event handlers can be registered for"""

    GENERIC = "generic"

    # Messages - Sent
    CHANNEL_MESSAGE_SENT = "channel_message"
    PRIVATE_MESSAGE_SENT = "private_message"
    MESSAGE_SENT         = "message"

    # Messages - Edited/Deleted
    MESSAGE_DELETED         = "message_deleted"
    MESSAGE_EDITED          = "message_edited"
    CHANNEL_MESSAGE_DELETED = "channel_message_deleted"
    CHANNEL_MESSAGE_EDITED  = "channel_message_edited"
    PRIVATE_MESSAGE_DELETED = "private_message_deleted"
    PRIVATE_MESSAGE_EDITED  = "private_message_edited"

    # Commands
    COMMAND_SENT = "command_sent"

    # Channels
    CHANNEL_DELETED = "channel_deleted"
    CHANNEL_CREATED = "channel_created"
    CHANNEL_UPDATED = "channel_updated"

    # Members
    MEMBER_JOINED              = "member_joined"
    MEMBER_LEFT                = "member_left"
    MEMBER_UPDATED             = "member_updated"
    MEMBER_BANNED              = "member_banned"
    MEMBER_UNBANNED            = "member_unbanned"
    MEMBER_VOICE_STATE_UPDATED = "member_voice_state_updated"
    MEMBER_TYPING              = "member_typing"

    # Servers
    SERVER_JOINED       = "server_joined"
    SERVER_LEFT         = "server_left"
    SERVER_UPDATED      = "server_updated"
    SERVER_AVAILABLE    = "server_available"
    SERVER_UNAVAILABLE  = "server_unavailable"
    SERVER_ROLE_CREATED = "server_role_created"
    SERVER_ROLE_DELETED = "server_role_deleted"
    SERVER_ROLE_UPDATED = "server_role_updated"

    # Client Status
    CLIENT_READY = "on_ready"
