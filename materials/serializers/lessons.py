from rest_framework import serializers
from materials.models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title', 'image', 'description', 'video_link', 'course',]
