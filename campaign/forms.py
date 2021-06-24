import datetime
from django import forms
from django.core.exceptions import ValidationError

from .models import Campaign, Comment


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('name', 'description', 'category', 'youtube_id', 'goal', 'expiration_date', 'tags', )
        widgets = {
            'expiration_date': forms.DateInput(attrs={
                'type': 'date',
            })
        }

    def clean_expiration_date(self):
        expiration_date = self.cleaned_data['expiration_date']

        if expiration_date < datetime.date.today():
            raise ValidationError('Invalid date - expiration in past')

        return expiration_date

    def clean_goal(self):
        goal = self.cleaned_data['goal']

        if goal < 0:
            raise ValidationError('Invalid goal - amount is less than zero')

        return goal


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
            })
        }
        labels = {
            'content': '',
        }


class CampaignImageForm(forms.Form):
    images = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'multiple': True,
        'class': 'dropzone'}))
