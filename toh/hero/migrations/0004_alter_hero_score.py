# Generated by Django 3.2.6 on 2021-10-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_hero_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='score',
            field=models.IntegerField(default=100),
        ),
    ]