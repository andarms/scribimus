from django.contrib import admin

from .models import StoryCategory, Story


admin.site.register(StoryCategory)
admin.site.register(Story)
