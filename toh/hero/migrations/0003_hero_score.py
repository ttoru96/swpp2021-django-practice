# Generated by Django 3.2.5 on 2021-10-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_auto_20211014_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
