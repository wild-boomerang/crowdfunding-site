from django import forms

from .models import Campaign, Comment


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('name', 'description', 'category', 'youtube_id', 'goal', 'expiration_date', 'tags', )
        widgets = {
            'expiration_date': forms.DateInput(attrs={
                # 'class': 'form-control',
                'type': 'date',
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
