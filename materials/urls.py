from django.urls import path, include
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from materials.views.courses import CourseViewSet
from materials.views.lessons import LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet,)

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view()),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
]

urlpatterns += router.urls
