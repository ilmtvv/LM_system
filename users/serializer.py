from rest_framework import serializers, request
from rest_framework.permissions import IsAuthenticated

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, source='payment_set', default=[], read_only=True)

    class Meta:

        model = User
        fields = '__all__'
