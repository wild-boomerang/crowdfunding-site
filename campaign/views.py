from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from campaign.models import Campaign, CampaignCategory
from campaign.forms import CampaignForm


def campaign_list(request, category_slug=None):
    categories = CampaignCategory.objects.all()
    campaigns = Campaign.objects.all()
    category = None
    if category_slug:
        category = get_object_or_404(CampaignCategory, slug=category_slug)
        campaigns = campaigns.filter(category=category)

    return render(request, 'campaign/list.html', {'categories': categories,
                                                  'category': category,
                                                  'campaigns': campaigns})


def campaign_detail(request, author_slug, name_slug):
    campaign = get_object_or_404(Campaign, author_slug=author_slug, name_slug=name_slug)
    return render(request, 'campaign/detail.html', {'campaign': campaign})


@login_required
def campaign_new(request):
    if request.method == 'POST':
        campaign_form = CampaignForm(data=request.POST)
        if campaign_form.is_valid():
            campaign = campaign_form.save(commit=False)
            campaign.author = request.user
            campaign.save()
            return redirect('dashboard', username=request.user.username)
    else:
        campaign_form = CampaignForm()

    return render(request, 'campaign/new.html', {'campaign_form': campaign_form})
