# Generated by Django 3.2 on 2021-05-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_campaign_collected'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='campaign',
            constraint=models.UniqueConstraint(fields=('author', 'name'), name='uniqueAuthorPlusName'),
        ),
    ]
