from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsListAPIView

router = DefaultRouter()
router.register(r'', UserViewSet,)

app_name = UsersConfig.name

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view())
] + router.urls
