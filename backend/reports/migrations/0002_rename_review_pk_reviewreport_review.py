# Generated by Django 3.2.9 on 2021-11-23 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewreport',
            old_name='review_pk',
            new_name='review',
        ),
    ]