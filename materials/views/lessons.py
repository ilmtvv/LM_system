from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.paginators import MyPagination
from materials.permissions import UserisOwner
from materials.serializers.lessons import LessonSerializer
from materials.validators import validate_youtube_url
from users.permissions import UserPermissionsManager


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MyPagination
    def get_queryset(self):
        if self.request.user.groups.filter(pk=1).exists():
            queryset = Lesson.objects.all()
        else:
            queryset = Lesson.objects.all().filter(owner=self.request.user.pk)
        return queryset


class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, UserPermissionsManager | UserisOwner]


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~UserPermissionsManager]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.pk)

        # lesson = serializer.save(owner=self.request.user.pk)
        # description = lesson.description
        # validate_youtube_url(description)


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, UserPermissionsManager | UserisOwner]


class LessonDestroyAPIView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, UserisOwner, ~UserPermissionsManager]
