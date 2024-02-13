from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView


from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer




class CourseViewSet(viewsets.ViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

# class CourseListAPIView(ListAPIView):
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all()