# Generated by Django 3.2 on 2021-06-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0017_commentlike'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='commentlike',
            constraint=models.UniqueConstraint(fields=('author', 'comment'), name='uniqueAuthorPlusComment'),
        ),
    ]
