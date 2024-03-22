from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, PaymentCourse
from materials.serializers.lessons import LessonSerializer
from materials.validators import validate_youtube_url
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer


class CourseSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[validate_youtube_url])
    count_lessons = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, source='lesson_set', read_only=True)
    subscription = SerializerMethodField(read_only=True)

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    def get_subscription(self, obj):
        if Subscription.objects.all().filter(course=obj):
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = ['title', 'count_lessons', 'lessons', 'description', 'subscription']


class PayCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCourse
        fields = '__all__'
