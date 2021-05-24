from django import forms

from .models import Campaign


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('name', 'description', 'category', 'youtube_url', 'goal', 'expiration_date')
