from django.contrib import admin
from django.db import models

from martor.widgets import AdminMartorWidget

from .models import Campaign, CampaignImage, Bonus, CampaignCategory, Comment, CommentLike


@admin.register(CampaignCategory)
class CampaignCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'description', 'category', 'youtube_id', 'goal', 'collected', 'expiration_date',
                    'author_slug', 'name_slug')
    list_filter = ('author', 'category', 'expiration_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'expiration_date'
    ordering = ('expiration_date', 'author')
    # prepopulated_fields = {'slug': ('author', 'name')}
    raw_id_fields = ('author', )
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(CampaignImage)
class CampaignImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'image', 'campaign')
    list_filter = ('campaign', )
    search_fields = ('campaign', 'alt', 'image')
    ordering = ('campaign', 'alt', 'image')
    raw_id_fields = ('campaign', )


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'campaign', 'purchaser', 'price')
    list_filter = ('campaign', 'purchaser')
    search_fields = ('name', 'description', 'price')
    ordering = ('purchaser', 'campaign', 'name')
    raw_id_fields = ('purchaser', 'campaign')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'campaign', 'created', 'updated', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author', 'content')
    raw_id_fields = ('author', 'campaign')


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('is_like', 'author', 'comment')
    list_filter = ('is_like', 'author', 'comment')
    search_fields = ('author', 'comment')
    raw_id_fields = ('author', 'comment')
