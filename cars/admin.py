from django.contrib import admin
from django.utils.html import format_html
from .models import Car

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):  # لاسخراج الصوره 
        return format_html(f'<img src="{object.car_photo.url}" width="50" style="border-radius: 50px;" />')

    thumbnail.short_description = 'photo'


    list_display = ('id', 'car_title', 'thumbnail', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'car_title', 'thumbnail')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'fuel_type')
    list_filter = ('city',)

admin.site.register(Car, CarAdmin)
