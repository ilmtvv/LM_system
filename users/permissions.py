from rest_framework import permissions


class UserPermissionsCreate(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return False

class UserPermissionsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists():
            return True
        else:
            return False
