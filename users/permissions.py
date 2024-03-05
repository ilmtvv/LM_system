from rest_framework import permissions


class UserPermissionsManager(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(pk=1).exists():
            return True
        else:
            return False


class UserIsOwnerPay(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

            return request.user == obj.user

class UserIsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

            return request.user.pk == obj.user_pk
