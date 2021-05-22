from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from users.forms import CustomUserCreationForm


def dashboard(request):
    return render(request, 'account/dashboard.html')


class Home(TemplateView):
    template_name = 'home.html'
