# Generated by Django 3.2 on 2021-05-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0005_auto_20210523_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(max_length=300),
        ),
    ]