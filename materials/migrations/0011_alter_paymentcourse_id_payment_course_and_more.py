# Generated by Django 4.2.7 on 2024-03-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0010_alter_paymentcourse_id_payment_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcourse',
            name='id_payment_course',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name='paymentcourse',
            name='url_payment_course',
            field=models.URLField(default='', max_length=555),
        ),
    ]