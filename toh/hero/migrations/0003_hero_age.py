from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_auto_202110014_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]