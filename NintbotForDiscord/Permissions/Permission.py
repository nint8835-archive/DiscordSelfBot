from discord import Member

__author__ = 'Riley Flynn (nint8835)'


class Permission:
    def has_permission(self, member: Member) -> bool:
        return True


class PermissionGroup(Permission):
    permissions = [Permission()]

    def has_permission(self, member: Member) -> bool:
        return not any([not permission.has_permission(member) for permission in self.permissions])


class MatchAnyPermissionGroup(PermissionGroup):
    def has_permission(self, member: Member) -> bool:
        return any([permission.has_permission(member) for permission in self.permissions])


def create_permission_group(permissions) -> PermissionGroup:
    group = PermissionGroup()
    group.permissions = permissions
    return group


def create_match_any_permission_group(permissions) -> MatchAnyPermissionGroup:
    group = MatchAnyPermissionGroup()
    group.permissions = permissions
    return group
