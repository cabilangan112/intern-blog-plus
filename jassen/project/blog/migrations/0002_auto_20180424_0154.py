# Generated by Django 2.0.4 on 2018-04-24 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sub_Title',
            new_name='sub_title',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='vote',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
