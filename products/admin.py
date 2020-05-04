from django.contrib import admin
from .models import Brand, Category, Unit, Products


# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Products)
