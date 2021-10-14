from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_hero_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]