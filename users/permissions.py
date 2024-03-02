from rest_framework import permissions


class UserPermissionsCreate(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.method == permissions.SAFE_METHODS



class UserPermissionsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists():
            return True
        else:
            return False

class UserIsOwnerPay(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

            return request.user == obj.user

