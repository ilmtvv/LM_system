from rest_framework import viewsets
from materials.models import Course
from materials.serializers.courses import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
