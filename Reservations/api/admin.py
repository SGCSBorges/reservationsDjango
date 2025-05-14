from django.contrib import admin

# Register your models here.
from .models import APIKey

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'tier', 'created_at')
    list_filter = ('tier',)
    search_fields = ('user__username', 'key')