# -*- coding: utf-8 -*
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.safestring import SafeUnicode
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	@models.permalink
	def get_absolute_url(self):
		return ('pages_tag', (), {'slug': self.slug})

	class Meta:
		ordering = ['name']
		verbose_name = _('Tag')
		verbose_name_plural = _('Tags')

	def __unicode__(self):
		return self.name


class Page(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	header = models.CharField(verbose_name=_('Header'), max_length=256)
	keywords = models.CharField(verbose_name=_('Keywords'), max_length=1024, blank=True, null=True)
	description = models.CharField(verbose_name=_('Description'), max_length=2048, blank=True, null=True)

	intro = models.TextField(verbose_name=_('Intro'), blank=True, null=True)
	text = models.TextField(verbose_name=_('Text'), blank=True, null=True)

	img = models.FileField(verbose_name=_('Image'), upload_to='img/pages', blank=True)

	per_page = models.IntegerField(verbose_name=_('Items per page'), help_text=_('The maximum number of items to include on a page'), default=10)
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	template = models.CharField(verbose_name=_('Template'), max_length=32, null=True, blank=True)

	level = models.IntegerField(verbose_name=_('Level'), default=0, editable=False)
	order = models.IntegerField(verbose_name=_('Order'), default=500, blank=True, null=True)
	real_order = models.IntegerField(verbose_name=_('Real Order'), default=500, blank=True, null=True, editable=False)

	tags = models.ManyToManyField(Tag, related_name='pages', verbose_name=_('Tags'), null=True, blank=True)
	# Fix: related_name
	sites = models.ManyToManyField(Site, related_name='pagess', verbose_name=_('Sites'), null=True, blank=True)
	slug = models.CharField(verbose_name=_('Slug'), max_length=256, default='#')
	url = models.CharField(verbose_name=_('URL'), max_length=1024, editable=False)

	main = models.BooleanField(verbose_name=_('Main'), default=False)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	# def get_childs(self):
	# 	childs = []

	# 	for category in Category.objects.filter(public=True, parent=self.id):
	# 		for category_id in category.get_all():
	# 			childs.append(category_id)

	# 	return childs

	# def get_all(self):
	# 	return [self.id] + self.get_childs()

	def all_childs(self):
		childs = []
		print self
		for child in self.childs.all():
			childs.append(child)
			childs += child.all_childs()

		return childs

	def get_absolute_url(self):
		return self.url

	def get_level(self):
		if settings.APPEND_SLASH:
			minus_slash = 2
		else:
			minus_slash = 1

		level = self.url.count('/') - minus_slash
		return level

	def __unicode__(self):
		padding = self.level * 4
		display = '&nbsp;' * padding + self.title
		return SafeUnicode(display)

	def resort(self, parent, i):
		if parent:
			pages = Page.objects.filter(parent=parent)
		else:
			pages = Page.objects.filter(parent__isnull=True)

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
			self.resort(0, 0)

	class Meta:
		ordering = ['real_order']
		# ordering = ['level', 'order']
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')

	# def get_next(self):
	# 	next = Page.objects.filter(id__gt=self.id, category=self.category, public=True)
	# 	if next:
	# 		return next[0]
	# 	return False

	# def get_prev(self):
	# 	prev = Page.objects.filter(id__lt=self.id, category=self.category, public=True)
	# 	if prev:
	# 		return prev[0]
	# 	return False
