from django.contrib import admin

# Register your models here.
from .models import RSSFeed

@admin.register(RSSFeed)
class RSSFeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active')
    prepopulated_fields = {'slug': ('title',)}