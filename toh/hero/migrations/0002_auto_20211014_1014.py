from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]