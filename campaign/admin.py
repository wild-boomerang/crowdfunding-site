from django.contrib import admin

from .models import Campaign, CampaignImage, Bonus, CampaignCategory


@admin.register(CampaignCategory)
class CampaignCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'description', 'category', 'youtube_url', 'goal', 'collected', 'expiration_date', 'slug')
    list_filter = ('author', 'category', 'expiration_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'expiration_date'
    ordering = ('expiration_date', 'author')
    prepopulated_fields = {'slug': ('author', 'name')}
    raw_id_fields = ('author', )


@admin.register(CampaignImage)
class CampaignImageAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'alt', 'image')
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
