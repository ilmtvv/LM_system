from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course
from materials.permissions import UserisOwner
from materials.serializers.courses import CourseSerializer
from users.permissions import UserPermissionsManager


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.pk)

    def get_permissions(self):
        if self.action == 'delete' or self.action == 'create':
            self.permission_classes = [UserPermissionsManager]
        elif self.action == 'update':
            self.permission_classes = [UserPermissionsManager & UserisOwner]
        return [permission() for permission in self.permission_classes]