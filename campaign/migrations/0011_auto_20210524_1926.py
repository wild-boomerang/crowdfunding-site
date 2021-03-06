# Generated by Django 3.2 on 2021-05-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0010_alter_campaignimage_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='slug',
        ),
        migrations.AddField(
            model_name='campaign',
            name='author_slug',
            field=models.SlugField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='campaign',
            name='name_slug',
            field=models.SlugField(blank=True, max_length=300),
        ),
    ]
