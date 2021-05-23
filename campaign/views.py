import types

from django.shortcuts import render, get_object_or_404

from campaign.models import Campaign, CampaignCategory


def campaign_list(request, category_slug=None):
    categories = CampaignCategory.objects.all()
    campaigns = Campaign.objects.all()
    category = None
    if category_slug:
        category = get_object_or_404(CampaignCategory, slug=category_slug)
        campaigns = campaigns.filter(category=category)

    return render(request, 'campaign/list.html', {'categories': categories, 'category': category,
                                                  'campaigns': campaigns})


def campaign_detail(request, campaign_slug):
    campaign = get_object_or_404(Campaign, slug=campaign_slug)
    return render(request, 'campaign/detail.html', {'campaign': campaign})
