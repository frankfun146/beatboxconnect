from .forms import form

from django.shortcuts import render, redirect
from django.http import request


# Create your views here.


def home(request):
    context = {}
    return render(request, 'main/home.html', context)


def contact(request):
    if request.method == 'POST':
        user_form = form(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'main/contact_success.html', {})
    else:
        user_form = form()
        context = {'form': user_form}
        return render(request, 'main/contact.html', context)


def contact_success(request):
    return render(request, 'main/contact_success.html', {})
