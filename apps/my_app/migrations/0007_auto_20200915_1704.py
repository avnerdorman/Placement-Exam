# Generated by Django 3.1.1 on 2020-09-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_remove_friend_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='exam',
            field=models.JSONField(default='{}'),
        ),
    ]
