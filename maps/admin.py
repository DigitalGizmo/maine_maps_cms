from django.contrib import admin
from .models import MapSet, MapView


class MapViewInline(admin.TabularInline):
    model = MapView
    extra = 1
    fields = [
        'ordinal', 'filename', 'caption', 'interpretive_text',
        'is_crop', 'crop_x', 'crop_y', 'crop_width', 'crop_height',
        'image_width', 'image_height',
    ]


@admin.register(MapSet)
class MapSetAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [MapViewInline]
