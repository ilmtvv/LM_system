from celery import shared_task
from django.core.mail import send_mail
from rest_framework import viewsets, request
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from config.settings import EMAIL_HOST_USER
from config.tasks import update_notification
from materials.models import Course, PaymentCourse
from materials.paginators import MyPagination
from materials.permissions import UserisOwner
from materials.serializers.courses import CourseSerializer, PayCourseSerializer
from materials.utils import create_product, create_pay_course, create_pay_session
from subscription.models import Subscription
from users.permissions import UserPermissionsManager


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MyPagination

    # def update(self, request, *args, **kwargs):
    #     pass

    def perform_update(self, serializer):
        course_id = int(self.kwargs['pk'])
        #print(course_id)
        emails = []
        subs_item = Subscription.objects.all().filter(course=course_id)
        for email in subs_item:
            emails.append(email.user.email)
        #print(emails)


        update_notification(emails)

        serializer.save()

    def list(self, request, *args, **kwargs):

        if self.request.user.groups.filter(pk=1).exists():
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(self.get_queryset().filter(owner=self.request.user.pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.pk)


    def get_permissions(self):
        list_of_permission = ('destroy', 'create', 'update', 'retrieve')
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~UserPermissionsManager]
        if self.action == 'update':
            self.permission_classes = [IsAuthenticated, UserPermissionsManager | UserisOwner]
        if self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, UserisOwner]
        if self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, UserPermissionsManager | UserisOwner]

        return [permission() for permission in self.permission_classes]


class PayCourseCreateAPIView(CreateAPIView):
    serializer_class = PayCourseSerializer
    queryset = PaymentCourse.objects.all()
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        pay = serializer.save()

        id_product, amount = create_product(pay.course.pk)

        pay_course = create_pay_course(id_product, amount)

        pay.id_payment_course, pay.url_payment_course = create_pay_session(pay_course)

        pay.save()
