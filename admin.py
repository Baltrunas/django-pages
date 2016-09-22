from django.contrib import admin

from apps.files.admin import FileInline

from .models import Tag
from .models import Page


class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	save_as = True

admin.site.register(Tag, TagAdmin)


class PageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'slug', 'url', 'order', 'public', 'main']
	search_fields = ['title', 'slug', 'url', 'public', 'text']
	list_filter = ['public', 'main', 'sites', 'parent']
	list_editable = ['order', 'public', 'main']
	inlines = [FileInline]
	save_as = True

admin.site.register(Page, PageAdmin)




from .models import Block, SubBlock


class SubBlockInline(admin.StackedInline):
	model = SubBlock
	extra = 0


class BlockAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'order', 'public']
	search_fields = ['title', 'slug', 'order', 'public']
	list_filter = ['public', 'pages']
	list_editable = ['public', 'order']
	inlines = [SubBlockInline]

admin.site.register(Block, BlockAdmin)


class SubBlockAdmin(admin.ModelAdmin):
	list_display = ['title', 'block', 'sub_title', 'order', 'public']
	search_fields = ['title', 'block', 'sub_title', 'order', 'public']
	list_filter = ['public']
	list_editable = ['public', 'order']

admin.site.register(SubBlock, SubBlockAdmin)
