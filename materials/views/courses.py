from rest_framework import viewsets, request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Course
from materials.permissions import UserisOwner
from materials.serializers.courses import CourseSerializer
from users.permissions import UserPermissionsManager


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self, request, *args, **kwargs):

        if self.request.user.groups.filter(pk=1).exists():
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(self.get_queryset().filter(owner=self.request.user.pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.pk)

    def get_permissions(self):
        list_of_permission = ('destroy', 'create', 'update', 'retrieve')
        if self.action in list_of_permission:
            self.permission_classes = [UserisOwner]


        return [permission() for permission in self.permission_classes]
