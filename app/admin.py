from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SocialLink)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['photo', 'name', 'age', 'job']
    search_fields = ['name', 'age', 'job', 'technologies', 'languages']
    list_per_page = 10


admin.site.register(Visitors)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'photo']
    search_fields = ['title']
    list_per_page = 10


admin.site.register(Info)
