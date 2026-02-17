from django.contrib import admin
from .models import MapSet, MapView


@admin.register(MapSet)
class MapSetAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(MapView)
class MapViewAdmin(admin.ModelAdmin):
    list_display = ['caption', 'mapset', 'ordinal', 'filename', 'is_crop']
    list_filter = ['mapset']
    fields = [
        'mapset', 'ordinal', 'filename', 'caption', 'interpretive_text',
        'is_crop', 'crop_x', 'crop_y', 'crop_width', 'crop_height',
        'image_width', 'image_height',
    ]
