from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = User.objects.create(
            username='admin',
            email='admin@admin.com',
            is_staff=True,
            is_superuser=True
        )
        admin.set_password('123qwe456rty')
        admin.user_pk = admin
        admin.save()
        manager = User.objects.create(
            username='manager',
            email='manager@manager.com',
            is_staff=True,
            is_superuser=False,

        )
        manager.groups.set((1,))
        manager.set_password('123qwe456rty')
        manager.user_pk = manager
        manager.save()

        user = User.objects.create(
            username='user',
            email='user@user.com',

        )
        user.set_password('123qwe456rty')
        user.user_pk = user
        user.save()
