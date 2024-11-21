# Register your models here.
from django.contrib import admin

from .models import Category, Region, New


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'region', 'date', 'author')
    list_filter = ('category', 'region', 'date')
    search_fields = ('title', 'text')
    date_hierarchy = 'date'


admin.site.register(Category)
admin.site.register(Region)
admin.site.register(New)
