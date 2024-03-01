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
        admin.save()

        manager = User.objects.create(
            username='manager',
            email='manager@manager.com',
            is_staff=True,
            is_superuser=False,
            groups=[1,]
        )
        manager.set_password('123qwe456rty')
        manager.save()
