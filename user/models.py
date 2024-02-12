from django.contrib.auth.models import AbstractUser
from django.db import models

null_blank = {'null': True, 'blank': True}

class User(AbstractUser):
    username = models.CharField(max_length=25, default='user')
    email = models.EmailField()
    phone = models.CharField(max_length=11, **null_blank)
    city = models.CharField(max_length=25, **null_blank)
    avatar = models.ImageField(upload_to='user/', **null_blank)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
