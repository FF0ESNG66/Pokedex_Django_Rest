from rest_framework import permissions


class AdminOnlyPermissions(permissions.DjangoModelPermissions):
    
    perms_map = {
        'GET': [], 
        'OPTIONS': ['%(app_label)s.options_%(model_name)s'],
        'HEAD': ['%(app_label)s.head_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
        }
    

