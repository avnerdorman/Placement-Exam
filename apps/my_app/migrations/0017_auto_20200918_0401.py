# Generated by Django 3.1.1 on 2020-09-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0016_remove_friend_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='next_question',
            field=models.CharField(default='next', max_length=100),
        ),
        migrations.AddField(
            model_name='friend',
            name='previous_question',
            field=models.CharField(default='previous', max_length=100),
        ),
    ]
