from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from users.forms import CustomUserCreationForm


def dashboard(request, username):
    requested_user = get_user_model().objects.get(username=username)

    return render(request, 'account/dashboard.html', {'author': requested_user})


class Home(TemplateView):
    template_name = 'home.html'
