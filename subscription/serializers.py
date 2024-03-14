from rest_framework import serializers
from materials.models import Lesson
from materials.validators import validate_youtube_url
from subscription.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
