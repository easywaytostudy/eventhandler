# Generated by Django 2.2 on 2019-05-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_createevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='createevent',
            name='time',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
