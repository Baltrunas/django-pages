from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from apps.files.models import File

from .models import Tag
from .models import Page


class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	save_as = True

admin.site.register(Tag, TagAdmin)


class FileInline(GenericTabularInline):
	model = File
	extra = 3


class PageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'slug', 'url', 'order', 'public', 'main']
	search_fields = ['title', 'slug', 'url', 'public', 'text']
	list_filter = ['public', 'main', 'sites', 'parent']
	list_editable = ['order', 'public', 'main']
	inlines = [FileInline]
	save_as = True

admin.site.register(Page, PageAdmin)
