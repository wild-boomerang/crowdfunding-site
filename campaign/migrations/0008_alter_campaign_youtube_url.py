# Generated by Django 3.2 on 2021-05-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0007_auto_20210523_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='youtube_url',
            field=models.URLField(blank=True),
        ),
    ]