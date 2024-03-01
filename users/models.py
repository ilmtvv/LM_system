from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

null_blank = {'null': True, 'blank': True}


class User(AbstractUser):
    username = models.CharField(max_length=25, default='users')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, **null_blank)
    city = models.CharField(max_length=25, **null_blank)
    avatar = models.ImageField(upload_to='images/users', **null_blank)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    data_of_payment = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=0)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, default=0)
    amount = models.FloatField(default=11)
    payment_method = models.CharField(max_length=11, default='transfer')

    def __str__(self):
        return f'{self.data_of_payment}'
