from django import template
from django.shortcuts import get_object_or_404

from campaign.models import Campaign

register = template.Library()


@register.simple_tag
def get_percent(pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return round(campaign.collected / campaign.goal * 100) if campaign.collected != 0 else 0


@register.simple_tag
def define(val=None):
    return val
