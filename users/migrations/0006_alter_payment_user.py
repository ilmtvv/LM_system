# Generated by Django 4.2.7 on 2024-02-24 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payment_data_of_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(default=[], on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
