# Generated by Django 3.1.1 on 2020-09-18 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0014_auto_20200915_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
