# Generated by Django 3.2.7 on 2021-10-15 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_hero_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
