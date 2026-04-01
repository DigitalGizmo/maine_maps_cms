from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteInplaceWidget
from .models import MapSet, MapView


class ShortSummernoteWidget(SummernoteInplaceWidget):
    def summernote_settings(self):
        settings = super().summernote_settings()
        settings['height'] = 120
        return settings


@admin.register(MapSet)
class MapSetAdmin(SummernoteModelAdmin):
    summernote_fields = ('credit',)

    def formfield_for_dbfield(self, db_field, *args, **kwargs):
        if db_field.name == 'credit':
            kwargs['widget'] = ShortSummernoteWidget
        return super().formfield_for_dbfield(db_field, *args, **kwargs)
    list_display = ['title', 'slug','map_orientation', 'aspect_ratio']
    prepopulated_fields = {'slug': ('title',)}
    fields = ['title', 'short_title', 'slug', 'date', 'short_description',
              'map_orientation', 'aspect_ratio', 'credit']


@admin.register(MapView)
class MapViewAdmin(SummernoteModelAdmin):
    summernote_fields = ('interpretive_text',)
    list_display = ['title', 'mapset', 'ordinal', 'filename', 'is_crop']
    list_filter = ['mapset']
    fields = [
        'mapset', 'ordinal', 'filename', 'title', 'interpretive_text',
        'image_width', 'image_height',
        'is_crop', 'crop_x', 'crop_y', 'crop_width', 'crop_height',
        
    ]
