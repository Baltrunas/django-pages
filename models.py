from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.safestring import SafeUnicode
from django.utils.translation import ugettext as _

from helpful.fields import upload_to


class Tag(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, unique=True, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	def pages_count(self):
		return self.pages.filter(public=True).count()

	@models.permalink
	def get_absolute_url(self):
		return ('pages_tag', (), {'slug': self.slug})

	class Meta:
		ordering = ['name']
		verbose_name = _('Tag')
		verbose_name_plural = _('Tags')

	def __unicode__(self):
		return self.name


# class URL(models.Model):
	# title = models.CharField(verbose_name=_('Title'), max_length=256)
	# url = models.CharField(verbose_name=_('URL or URL RegEx'), max_length=2048)
	# regex = models.BooleanField(verbose_name=_('RegEx'), default=False)

	# created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	# updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	# def __unicode__(self):
	# 	return self.title

	# class Meta:
	# 	ordering = ['-created_at']
	# 	verbose_name = _('URL')
	# 	verbose_name_plural = _('URLs')
class Page(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	header = models.CharField(verbose_name=_('Header'), max_length=256)
	keywords = models.CharField(verbose_name=_('Keywords'), max_length=1024, blank=True, null=True)
	description = models.CharField(verbose_name=_('Description'), max_length=2048, blank=True, null=True)

	intro = models.TextField(verbose_name=_('Intro'), blank=True, null=True)
	text = models.TextField(verbose_name=_('Text'), blank=True, null=True)

	img = models.FileField(verbose_name=_('Image'), upload_to=upload_to, blank=True)

	per_page = models.IntegerField(verbose_name=_('Items per page'), help_text=_('The maximum number of items to include on a page'), default=10)
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	template = models.CharField(verbose_name=_('Template'), max_length=32, null=True, blank=True)

	level = models.IntegerField(verbose_name=_('Level'), default=0, editable=False)
	order = models.IntegerField(verbose_name=_('Order'), default=500, blank=True, null=True)
	real_order = models.IntegerField(verbose_name=_('Real Order'), default=500, blank=True, null=True, editable=False)

	tags = models.ManyToManyField(Tag, related_name='pages', verbose_name=_('Tags'), blank=True)
	sites = models.ManyToManyField(Site, related_name='pages', verbose_name=_('Sites'), blank=True)
	slug = models.CharField(verbose_name=_('Slug'), max_length=256, default='#')
	url = models.CharField(verbose_name=_('URL'), max_length=1024, editable=False)

	# blocks = models.ManyToManyField('Block', verbose_name=_('Blocks'), blank=True, related_name='pages')

	main = models.BooleanField(verbose_name=_('Main'), default=False)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)



	def __init__(self, *args, **kwargs):
		super(Page, self).__init__(*args, **kwargs)
		self._prev_parent = self.parent
		self._prev_level = self.level
		self._prev_order = self.order

	def group(self):
		groups = {}
		block_groups = self.blocks.order_by('group').distinct().values_list('group', flat=True)
		for group in block_groups:
			groups[group] = self.blocks.filter(group=group, public=True)
		return groups

	def all_childs(self):
		childs = []
		for child in self.childs.all():
			childs.append(child)
			childs += child.all_childs()

		return childs

	def sub_tags(self):
		tags = []
		for page in self.childs.all():
			for tag in page.tags.all():
				tags.append(tag)

		tags = Tag.objects.filter(pk__in=[tag.id for tag in tags])
		return tags

	def get_level(self):
		if settings.APPEND_SLASH:
			minus_slash = 2
		else:
			minus_slash = 1

		level = self.url.count('/') - minus_slash
		return level

	def resort(self, parent, i):
		if parent:
			pages = Page.objects.filter(parent=parent).order_by('order')
		else:
			pages = Page.objects.filter(parent__isnull=True).order_by('order')

		for page in pages:
			i += 1
			page.real_order = i
			page.save(sort=False)
			i = self.resort(page.id, i)
		return i

	def save(self, sort=True, *args, **kwargs):
		if self.parent:
			self.url = self.parent.url
			if not settings.APPEND_SLASH:
				self.url += '/'
		else:
			self.url = '/'

		self.url += self.slug

		if settings.APPEND_SLASH:
			self.url += '/'

		if self.slug == '/':
			self.url = '/'

		self.level = self.get_level()

		super(Page, self).save(*args, **kwargs)

		if sort:
			if self._prev_parent != self.parent or self._prev_order != self.order or self._prev_level != self.level:
				self.resort(0, 0)

	def __unicode__(self):
		padding = self.level * 4
		display = '&nbsp;' * padding + self.title
		return SafeUnicode(display)

	def get_absolute_url(self):
		return self.url

	class Meta:
		ordering = ['real_order', '-created_at']
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')


class Block(models.Model):
	slug = models.SlugField(_('Slug'), max_length=128)

	title = models.CharField(_('Title'), max_length=256, blank=True, null=True)
	description = models.CharField(_('Description'), max_length=2048, blank=True, null=True)
	text = models.TextField(_('Text'), blank=True, null=True)

	image = models.FileField(_('Image'), upload_to=upload_to, blank=True, null=True)
	bg = models.FileField(_('Background'), upload_to=upload_to, blank=True, null=True)

	order = models.PositiveIntegerField(_('Sort ordering'), default=500)

	pages = models.ManyToManyField(Page, verbose_name=_('Pages'), related_name='blocks', blank=True)

	template = models.CharField(_('Template'), max_length=124, blank=True, null=True)
	group = models.CharField(_('Area'), max_length=64, default='content')

	public = models.BooleanField(_('Public'), default=True)
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

	def subblocks(self):
		return self.all_subblocks.filter(public=True)

	def __unicode__(self):
		if self.title:
			return self.title
		else:
			return self.slug

	class Meta:
		ordering = ['order']
		verbose_name = _('Block')
		verbose_name_plural = _('Blocks')


class SubBlock(models.Model):
	title = models.CharField(_('Title'), max_length=256, blank=True, null=True)
	description = models.CharField(_('Description'), max_length=2048, blank=True, null=True)
	text = models.TextField(_('Text'), blank=True, null=True)
	image = models.FileField(_('Image'), upload_to=upload_to, blank=True, null=True)

	order = models.PositiveIntegerField(_('Sort ordering'), default=500)


	block = models.ForeignKey(Block, verbose_name=_('Block'), related_name='all_subblocks')

	public = models.BooleanField(_('Public'), default=True)
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

	def dependent_from(self):
		return self.block

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['order']
		verbose_name = _('Sub block')
		verbose_name_plural = _('Sub blocks')






from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

class View(models.Model):
	content_type = models.ForeignKey(ContentType, verbose_name=_('Content Type'))
	object_id = models.PositiveIntegerField(_('Object ID'))
	content_object = GenericForeignKey('content_type', 'object_id')

	site = models.ForeignKey(Site, verbose_name=_('Site'), null=True, blank=True)
	referer = models.URLField(_('URL'), max_length=4096)
	user_agent = models.CharField(_('User agent'), max_length=4096)
	ip =  models.GenericIPAddressField(_('Site'), protocol='both', unpack_ipv4=False)
	url = models.URLField(_('URL'), max_length=4096)

	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), null=True, blank=True)

	datatime = models.DateTimeField(_('Date and time'), auto_now_add=True)
