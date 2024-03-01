from django.contrib.auth.models import Group
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from groups.serializer import GroupSerializer


class GroupsListAPIView(ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
