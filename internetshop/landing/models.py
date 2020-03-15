from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"Пользователь: {self.name} - {self.email}"

    class Meta:
        verbose_name = "MySubscriber"
        verbose_name_plural = "A lot of Subscribers"
