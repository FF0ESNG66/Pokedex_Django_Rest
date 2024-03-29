from rest_framework import permissions


class UserPermissions(permissions.DjangoModelPermissions):
    
    perms_map = {
        'GET': [], 
        'OPTIONS': ['%(app_label)s.options_%(model_name)s'],
        'HEAD': ['%(app_label)s.head_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
        }
    

class AllDenied(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
    

class AllowAnyAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False