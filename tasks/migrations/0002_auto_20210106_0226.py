# Generated by Django 3.1.2 on 2021-01-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]