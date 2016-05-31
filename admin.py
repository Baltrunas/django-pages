from django.contrib import admin

from .models import Tag
from .models import Page
from .models import Media

from apps.files.models import File
from django.contrib.contenttypes.admin import GenericTabularInline


class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	save_as = True

admin.site.register(Tag, TagAdmin)


class MediaAdmin(admin.ModelAdmin):
	list_display = ['name', 'page', 'order', 'public', 'created_at', 'updated_at']
	list_filter = ['name', 'page', 'type', 'group', 'order', 'public', 'created_at', 'updated_at']
	search_fields = ['name']

admin.site.register(Media, MediaAdmin)


class MediaInline(admin.TabularInline):
	model = Media
	extra = 3

class FileInline(GenericTabularInline):
	model = File
	extra = 3


class PageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'slug', 'url', 'order', 'public', 'main']
	search_fields = ['title', 'slug', 'url', 'public', 'text']
	list_filter = ['public', 'main', 'sites', 'parent']
	list_editable = ['order', 'public', 'main']
	inlines = [FileInline, MediaInline]
	save_as = True

admin.site.register(Page, PageAdmin)
