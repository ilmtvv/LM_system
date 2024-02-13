from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.apps import CoursesConfig
from courses.views import CourseViewSet

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
urlpatterns = [

] + router.urls
