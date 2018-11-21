from django.contrib import admin
from .models import Profile, Trade


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'ra', 'user', 'etec', 'course')
    list_display_links = ('id', 'user')
    search_fields = ('user.name', 'ra')
    list_per_page = 25

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Trade)
