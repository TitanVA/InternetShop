from django.contrib import admin
from . import models


class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in models.Subscriber._meta.fields]
    search_fields = ["name", "email"]
    # list_filter = ('email',)
    # exclude = ["email"]
    # inlines = [FieldMappingInLine]
    # fields = ["email"]
    # search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = models.Subscriber


admin.site.register(models.Subscriber, SubscriberAdmin)
