# Generated by Django 4.2.14 on 2024-08-26 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0010_alter_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
