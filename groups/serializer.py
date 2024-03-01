from django.contrib.auth.models import Group
from rest_framework import serializers, request
from rest_framework.permissions import IsAuthenticated

from users.models import User, Payment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

