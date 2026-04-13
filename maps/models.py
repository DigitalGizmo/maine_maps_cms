from django.db import models


class MapSet(models.Model):
    ORIENTATION_CHOICES = [
        ('vertical', 'Vertical'),
        ('horizontal', 'Horizontal'),
    ]

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=12, blank=True)
    short_description = models.CharField(max_length=500, blank=True)
    map_orientation = models.CharField(
        max_length=20,
        choices=ORIENTATION_CHOICES,
        default='vertical',
        help_text='Portrait layout: vertical maps set height; horizontal maps fill width'
    )
    aspect_ratio = models.CharField(
        max_length=20,
        default='3/5',
        help_text='CSS aspect-ratio value, e.g. "3/5" or "4/3"'
    )
    credit = models.TextField(
        blank=True,
        help_text='shift + enter for plain line return'
    )

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.slug + ": " + self.title


class MapView(models.Model):
    mapset = models.ForeignKey(
        MapSet, on_delete=models.CASCADE, related_name='views'
    )
    ordinal = models.PositiveIntegerField(
        verbose_name='View Number',
        help_text='1 = default full view, 2+ = detail/variation views'
    )
    filename = models.CharField(
        max_length=200,
        help_text='Base filename for tiles, e.g. 1700_3_1798'
    )
    title = models.CharField(max_length=200, blank=True)
    caption = models.CharField(max_length=500, blank=True)
    interpretive_text = models.TextField(
        blank=True,
        help_text='HTML subset: p, em, strong, ul, li'
    )
    is_crop = models.BooleanField(
        default=False,
        help_text='Whether this view shows a cropped detail'
    )
    crop_x = models.IntegerField(null=True, blank=True)
    crop_y = models.IntegerField(null=True, blank=True)
    crop_width = models.IntegerField(null=True, blank=True)
    crop_height = models.IntegerField(null=True, blank=True)

    # DZI metadata — needed for inline tile source (avoids CORS on .dzi fetch)
    image_width = models.IntegerField(
        null=True, blank=True,
        help_text='Full image width in pixels (from .dzi file)'
    )
    image_height = models.IntegerField(
        null=True, blank=True,
        help_text='Full image height in pixels (from .dzi file)'
    )

    class Meta:
        ordering = ['mapset', 'ordinal']
        unique_together = [['mapset', 'ordinal']]

    def __str__(self):
        return f'{self.mapset.title} — view {self.ordinal}'
