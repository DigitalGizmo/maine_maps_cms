from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MapSet, MapView


@admin.register(MapSet)
class MapSetAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','map_orientation', 'aspect_ratio']
    prepopulated_fields = {'slug': ('title',)}
    fields = ['title', 'short_title', 'slug', 'date', 'short_description', 
              'map_orientation', 'aspect_ratio']


@admin.register(MapView)
class MapViewAdmin(SummernoteModelAdmin):
    summernote_fields = ('interpretive_text',)
    list_display = ['caption', 'mapset', 'ordinal', 'filename', 'is_crop']
    list_filter = ['mapset']
    fields = [
        'mapset', 'ordinal', 'filename', 'caption', 'title', 'interpretive_text',
        'is_crop', 'crop_x', 'crop_y', 'crop_width', 'crop_height',
        'image_width', 'image_height',
    ]
