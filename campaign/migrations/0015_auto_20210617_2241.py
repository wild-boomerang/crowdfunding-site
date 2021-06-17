# Generated by Django 3.2 on 2021-06-17 19:41

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('campaign', '0014_campaign_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='author_slug',
            field=models.SlugField(max_length=300),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='name_slug',
            field=models.SlugField(max_length=300),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]