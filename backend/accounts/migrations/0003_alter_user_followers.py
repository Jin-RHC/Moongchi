# Generated by Django 3.2.9 on 2021-11-22 16:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
    ]
