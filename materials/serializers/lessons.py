from rest_framework import serializers
from materials.models import Lesson
from materials.validators import validate_youtube_url


class LessonSerializer(serializers.ModelSerializer):

    description = serializers.CharField(validators=[validate_youtube_url])

    class Meta:
        model = Lesson
        fields = ['title', 'image', 'description', 'video_link', 'course',]
