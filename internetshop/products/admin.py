from django.contrib import admin
from . import models


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = models.Product


admin.site.register(models.Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.ProductImage._meta.fields]

    class Meta:
        model = models.ProductImage


admin.site.register(models.ProductImage, ProductImageAdmin)
