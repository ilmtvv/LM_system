import datetime

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def update_notification(recipient_list):
    send_mail(
        'course_update',
        'course_update',
        EMAIL_HOST_USER,
        recipient_list,
    )


@shared_task
def active_user():

    current_datetime = datetime.timezone.now()
    one_month_ago = current_datetime - datetime.timedelta(days=30)

    users = User.objects.filter(last_login__lt=one_month_ago)
    for user in users:
        user.is_active = False
        user.save()
