from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from users.forms import CustomUserCreationForm


def dashboard(request):
    return render(request, 'account/dashboard.html')


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
    return render(request, 'registration/register.html', {'form': form})


class Home(TemplateView):
    template_name = 'home.html'
