# Generated by Django 3.2 on 2021-05-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_alter_bonus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='collected',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
