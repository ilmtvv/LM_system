from django.urls import path, include
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import LessonListAPIView, CourseViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet,)
urlpatterns = [
    path('lessons/', LessonListAPIView.as_view()),
    #path('course/', CourseListAPIView.as_view()),
]
urlpatterns += router.urls
