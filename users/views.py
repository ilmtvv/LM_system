from urllib import request

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from users.models import User, Payment
from users.permissions import UserPermissionsCreate, UserIsOwnerPay
from users.serializer import UserSerializer, PaymentSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermissionsCreate]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PaymentsListAPIView(ListAPIView):

    serializer_class = PaymentSerializer
    #queryset = Payment.objects.get(user=request.user)
    filter_backends = [OrderingFilter, DjangoFilterBackend,]
    ordering_fields = ('data_of_payment',)
    filterset_fields = ('lesson', 'course', 'payment_method')
    #permission_classes = [UserIsOwnerPay]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.pk)

    def get_queryset(self):
        queryset = Payment.objects.filter(user=self.request.user)
        return queryset
