from django.contrib import admin

from apps.models import Product, Category, Profile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
