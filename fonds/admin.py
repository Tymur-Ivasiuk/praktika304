from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin

from .models import *


class PhotoInlines(SortableTabularInline, admin.TabularInline):
    model = Photos
    extra = 1
    fields = ['image_tag','photo', 'my_order']
    readonly_fields = ['image_tag']

class FondsAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PhotoInlines
    ]

    list_display = ('id', 'title', 'desc', 'time_create', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class QuotesInline(admin.TabularInline):
    model = Quotes
    extra = 1
    fields = ['desc', 'author']

class SectionAdmin(admin.ModelAdmin):
    inlines = [
        QuotesInline
    ]
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Section, SectionAdmin)
admin.site.register(Fonds, FondsAdmin)