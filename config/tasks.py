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
    users = User.objects.all()
    for user in users:
        time_last_login = user.__dict__['last_login']
        if time_last_login:
            time_now = datetime.datetime.now().astimezone(datetime.timezone.utc)
            if datetime.timedelta(days=31) >= time_now - time_last_login:
                user.is_active = False
                user.save()
            else:
                user.is_active = True
                user.save()
