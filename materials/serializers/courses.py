from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course
from materials.serializers.lessons import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson_set', read_only=True)

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ['title', 'count_lessons', 'lessons']
