# Generated by Django 2.0.4 on 2018-04-24 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180424_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Comment',
        ),
    ]
