from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer
from users.permissions import UserPermissionsManager


class SubscriptionAPIView(APIView):
    """
    subscribe for own courses
    """
    permission_classes = [IsAuthenticated, ~UserPermissionsManager]
    def post(self, *args, **kwargs):
        user = self.request.user
        #print(self.request.data)
        course_id = self.request.data.get('course')
        course = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.all().filter(user=user, course=course)
        # print(subs_item)
        if subs_item.exists():
            # print(subs_item.exists())
            subs_item.delete()

            message = 'subscription delete'
        else:
            subs_item.create(user=user, course=course)

            message = 'start subscription'

        return Response({"message": message})
