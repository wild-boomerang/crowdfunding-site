# Generated by Django 3.2 on 2021-06-17 22:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0015_auto_20210617_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
