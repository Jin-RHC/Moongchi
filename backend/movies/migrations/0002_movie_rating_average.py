# Generated by Django 3.2.9 on 2021-11-24 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating_average',
            field=models.FloatField(blank=True, default=6),
            preserve_default=False,
        ),
    ]
