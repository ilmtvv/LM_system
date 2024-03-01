from django.urls import path

from groups.apps import GroupsConfig
from groups.views import GroupsListAPIView

app_name = GroupsConfig.name

urlpatterns = [
    path('', GroupsListAPIView.as_view()),

]
