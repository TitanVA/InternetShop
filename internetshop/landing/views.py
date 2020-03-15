from django.shortcuts import render
from . import forms
import datetime


def landing(request):
    form = forms.SubscriberForm(request.POST)
    now = datetime.datetime.now()
    if request.method == "POST" and form.is_valid():
        form = form.save()
    return render(request, 'landing/landing.html', locals())
