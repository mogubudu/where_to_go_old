from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)
    ordering = ('position',)

    def get_preview(self, obj):
        return format_html('<img src="{url}" width="{width}">',
                           url=obj.image.url,
                           width=200)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [
        PlaceImageInline,
    ]
