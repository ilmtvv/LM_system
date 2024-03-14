from django.db import models

from materials.models import Course
from users.models import User


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'
