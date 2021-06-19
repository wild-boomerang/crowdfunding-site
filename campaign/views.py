from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count

from campaign.models import Campaign, CampaignCategory, Comment, CommentLike
from campaign.forms import CampaignForm, CommentForm


def campaign_list(request, category_slug=None, tag_slug=None):
    categories = CampaignCategory.objects.all()
    campaigns = Campaign.objects.filter(active=True)
    category = None
    if category_slug:
        category = get_object_or_404(CampaignCategory, slug=category_slug)
        campaigns = campaigns.filter(active=True, category=category)

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        campaigns = campaigns.filter(active=True, tags__in=[tag])

    campaigns_num_per_page = 3
    paginator = Paginator(campaigns, campaigns_num_per_page)
    page_num = request.GET.get('page')

    try:
        campaigns = paginator.page(page_num)
    except EmptyPage:  # if page is out of range
        campaigns = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        campaigns = paginator.page(1)

    return render(request, 'campaign/list.html', {'categories': categories,
                                                  'category': category,
                                                  'tag': tag,
                                                  'campaigns': campaigns})


def campaign_detail(request, author_slug, name_slug):
    campaign = get_object_or_404(Campaign, author_slug=author_slug, name_slug=name_slug)
    comments = campaign.comments.filter(active=True)
    comment_form = CommentForm(data=request.POST or None)

    if request.method == 'POST':
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.campaign = campaign
            new_comment.save()
            return redirect('campaign:campaign_detail', author_slug, name_slug)

    campaign_tags_ids = campaign.tags.values_list('id', flat=True)
    similar_campaigns = Campaign.objects.filter(active=True, tags__in=campaign_tags_ids).exclude(id=campaign.id)
    similar_campaigns = similar_campaigns.annotate(same_tags=Count('tags')).order_by('-same_tags', '-updated')[:5]

    return render(request, 'campaign/detail.html', {'campaign': campaign,
                                                    'comment_form': comment_form,
                                                    'comments': comments,
                                                    'similar_campaigns': similar_campaigns})


def comment_edit(request, author_slug, name_slug, comment_pk):
    campaign = get_object_or_404(Campaign, author_slug=author_slug, name_slug=name_slug)
    comments = campaign.comments.filter(active=True)
    comment_to_edit = get_object_or_404(Comment, pk=comment_pk)
    comment_form = CommentForm(data=request.POST or None, instance=comment_to_edit)

    if request.method == 'POST':
        if comment_form.is_valid():
            comment_form.save()
            return redirect('campaign:campaign_detail', author_slug, name_slug)

    return render(request, 'campaign/detail.html', {'campaign': campaign,
                                                    'comment_form': comment_form,
                                                    'comments': comments,
                                                    'comment_to_edit': comment_to_edit})


def comment_delete(request, author_slug, name_slug, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()

    return redirect('campaign:campaign_detail', author_slug, name_slug)


@login_required
def process_like(request, author_slug, name_slug, comment_pk, like_type):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if like_type == 'like':
        is_like = True
    elif like_type == 'dislike':
        is_like = False
    else:
        raise Http404()

    like_obj, is_created = CommentLike.objects.get_or_create(author=request.user, comment=comment,
                                                             defaults={'is_like': is_like})

    if not is_created:
        if like_obj.is_like == is_like:  # user wants to delete like or dislike
            like_obj.delete()
        else:  # user wants to change like to dislike or vice versa
            like_obj.is_like = is_like
            like_obj.save()

    return redirect('campaign:campaign_detail', author_slug, name_slug)


@login_required
def campaign_new(request):
    if request.method == 'POST':
        campaign_form = CampaignForm(data=request.POST)
        if campaign_form.is_valid():
            campaign = campaign_form.save(commit=False)
            campaign.author = request.user
            campaign.save()
            return redirect('campaign:campaign_detail', campaign.author_slug, campaign.name_slug)
    else:
        campaign_form = CampaignForm()

    return render(request, 'campaign/new.html', {'campaign_form': campaign_form})


def campaign_edit(request, author_slug, name_slug):
    campaign = get_object_or_404(Campaign, author_slug=author_slug, name_slug=name_slug)
    campaign_form = CampaignForm(data=request.POST or None, instance=campaign)

    if request.method == 'POST':
        if campaign_form.is_valid():
            campaign_form.save()
            return redirect('campaign:campaign_detail', author_slug=campaign.author_slug, name_slug=campaign.name_slug)

    return render(request, 'campaign/new.html', {'campaign_form': campaign_form, 'campaign': campaign})


def campaign_delete(request, author_slug, name_slug):
    campaign = get_object_or_404(Campaign, author_slug=author_slug, name_slug=name_slug)
    campaign.delete()

    return redirect('campaign:campaign_list')
