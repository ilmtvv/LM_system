from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course
from materials.serializers.courses import CourseSerializer
from users.permissions import UserPermissionsManager


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [UserPermissionsManager]
        return [permission() for permission in self.permission_classes]