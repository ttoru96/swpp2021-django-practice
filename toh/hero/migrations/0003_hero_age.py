from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='age',
            field=models.IntegerField(defalut=25),
        ),
    ]