# Generated by Django 4.2.7 on 2024-02-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='data_of_payment',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data-of-pay'),
        ),
    ]