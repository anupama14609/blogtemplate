from django.contrib import admin
from .models import GenerateMeta

# Register your models here.
@admin.register(GenerateMeta)
class GenerateMetaAdmin(admin.ModelAdmin):
        list_display = ('title','description','keywords')
        list_display_links = ('title','description','keywords')
        list_per_page = 10
        search_fields = ('title',)
        