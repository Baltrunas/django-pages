from django.contrib import admin
from django.utils.translation import ugettext as _

# from apps.files.admin import FileInline

from .models import Tag
from .models import Page
from .models import Block


class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']
	save_as = True

admin.site.register(Tag, TagAdmin)



from django import forms
from django.db.models import Q


class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(PageForm, self).__init__(*args, **kwargs)
		self.fields['blocks'].queryset = Block.objects.filter(parent__isnull=True)


class PageAdmin(admin.ModelAdmin):
	form = PageForm
	list_display = ['__unicode__', 'slug', 'url', 'order', 'public', 'main']
	search_fields = ['title', 'slug', 'url', 'public', 'text']
	list_filter = ['public', 'main', 'sites', 'parent']
	list_editable = ['order', 'public', 'main']
	# inlines = [FileInline]
	save_as = True

admin.site.register(Page, PageAdmin)


class BlockForm(forms.ModelForm):
	class Meta:
		model = Block
		exclude = ['parent']

class BlockInline(admin.StackedInline):
	model = Block
	verbose_name = _('Sub block')
	verbose_name_plural = _('Sub blocks')
	extra = 0

class BlockAdmin(admin.ModelAdmin):
	form = BlockForm
	list_display = ['title', 'slug', 'order', 'public']
	search_fields = ['title', 'slug', 'order', 'public']
	list_filter = ['public']
	list_editable = ['public', 'order']
	inlines = [BlockInline]

admin.site.register(Block, BlockAdmin)
