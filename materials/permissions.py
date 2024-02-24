from rest_framework import permissions


class UserisOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user == view.owner:
            return True
        else:
            return False