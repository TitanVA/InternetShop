from django import forms
from .admin import models


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        exclude = [""]