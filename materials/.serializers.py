from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_youtube_url


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):

    description = serializers.CharField(validators=[validate_youtube_url])

    class Meta:
        model = Lesson
        fields = '__all__'
