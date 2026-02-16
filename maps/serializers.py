from rest_framework import serializers
from .models import MapSet, MapView


class MapViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapView
        fields = [
            'id', 'ordinal', 'filename', 'caption', 'interpretive_text',
            'is_crop', 'crop_x', 'crop_y', 'crop_width', 'crop_height',
            'image_width', 'image_height',
        ]


class MapSetSerializer(serializers.ModelSerializer):
    views = MapViewSerializer(many=True, read_only=True)

    class Meta:
        model = MapSet
        fields = ['id', 'slug', 'title', 'short_description', 'views']
