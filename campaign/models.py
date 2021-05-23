from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from crowdfundingsite import settings


class CampaignCategory(models.Model):
    # CATEGORY_CHOICES = (
    #     ('electronics', 'Electronics'),
    #     ('education', 'Education'),
    #     ('art', 'Art'),
    #     ('comics', 'Comics'),
    #     ('design', 'Design'),
    #     ('games', 'Games'),
    #     ('music', 'Music'),
    # )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name', )

    def get_absolute_url(self):
        return reverse('campaign:campaign_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Campaign(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='campaigns',
                               verbose_name='author')
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=300, db_index=True)
    description = models.TextField()
    category = models.ForeignKey(CampaignCategory, on_delete=models.CASCADE, related_name='campaigns')
    # tags = TaggableManager()
    youtube_url = models.URLField(max_length=200, blank=True)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    collected = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expiration_date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'name'], name='uniqueAuthorPlusName')
        ]

    def get_absolute_url(self):
        return reverse('campaign:campaign_detail', args=[self.slug])

    def __str__(self):
        return self.slug


class CampaignImage(models.Model):
    image = models.ImageField(upload_to='campaign_images', blank=True, null=True)
    alt = models.CharField('tip', max_length=100)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='images', verbose_name='campaign')

    def __str__(self):
        return self.alt


class Bonus(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='bonuses', verbose_name='campaign')
    purchaser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bonuses',
                                  verbose_name='purchaser')

    class Meta:
        verbose_name_plural = 'Bonuses'

    def __str__(self):
        return self.name
