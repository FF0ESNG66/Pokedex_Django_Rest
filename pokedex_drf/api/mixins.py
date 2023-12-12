from .permissions import AdminOnlyPermissions


class PermissionMixin():
    permission_classes = [
        AdminOnlyPermissions
    ]