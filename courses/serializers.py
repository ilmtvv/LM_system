from rest_framework import serializers

from courses.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'image', 'description', ]


class LessonSerializator(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'image', 'description', 'video_link', 'course', ]
