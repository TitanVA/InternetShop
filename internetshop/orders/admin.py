from django.contrib import admin
from . import models


class ProductInOrderInline(admin.TabularInline):
    model = models.ProductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Status._meta.fields]

    class Meta:
        model = models.Status


admin.site.register(models.Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Order._meta.fields]
    inlines = [ProductInOrderInline]

    class Meta:
        model = models.Order


admin.site.register(models.Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.ProductInOrder._meta.fields]

    class Meta:
        model = models.ProductInOrder


admin.site.register(models.ProductInOrder, ProductInOrderAdmin)