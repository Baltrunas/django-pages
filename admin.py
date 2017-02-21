from django.contrib import admin
from django.utils.translation import ugettext as _

# from apps.files.admin import FileInline

from .models import Tag
from .models import Page
from .models import Block
from .models import SubBlock


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
	# inlines = [FileInline]
	save_as = True

admin.site.register(Page, PageAdmin)


class SubBlockInline(admin.StackedInline):
	model = SubBlock
	verbose_name = _('Sub block')
	verbose_name_plural = _('Sub blocks')
	extra = 0

class BlockAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'slug', 'order', 'public']
	search_fields = ['title', 'slug', 'order', 'public']
	list_filter = ['public', 'pages', 'group']
	list_editable = ['public', 'order']
	inlines = [SubBlockInline]

admin.site.register(Block, BlockAdmin)
