from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
