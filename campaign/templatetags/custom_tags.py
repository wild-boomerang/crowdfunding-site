from django import template
from django.shortcuts import get_object_or_404

from campaign.models import Campaign, CommentLike

register = template.Library()


@register.simple_tag
def get_percent(pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return round(campaign.collected / campaign.goal * 100) if campaign.collected != 0 else 0


@register.simple_tag
def is_liked(author, comment, is_like):
    try:
        CommentLike.objects.get(author=author, comment=comment, is_like=is_like)
        return True
    except CommentLike.DoesNotExist:
        return False


@register.simple_tag
def get_likes(comment, is_like):
    return CommentLike.objects.filter(comment=comment, is_like=is_like).count()


@register.simple_tag
def define(val=None):
    return val
