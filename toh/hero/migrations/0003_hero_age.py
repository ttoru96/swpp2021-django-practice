# Generated by Django 3.2.8 on 2021-10-21 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
