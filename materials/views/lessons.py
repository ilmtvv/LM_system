from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.permissions import UserisOwner
from materials.serializers.lessons import LessonSerializer
from users.permissions import UserPermissionsManager


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        if self.request.user.groups.filter(pk=1).exists():
            queryset = Lesson.objects.all()
        else:
            queryset = Lesson.objects.all().filter(owner=self.request.user)
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


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, UserPermissionsManager | UserisOwner]


class LessonDestroyAPIView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, UserisOwner, ~UserPermissionsManager]
