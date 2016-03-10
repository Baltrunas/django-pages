from modeltranslation.translator import translator, TranslationOptions

from .models import Tag
from .models import Page
from .models import Media


class TagTranslationOptions(TranslationOptions):
	fields = ['name']

translator.register(Tag, TagTranslationOptions)


class PageTranslationOptions(TranslationOptions):
	fields = ['title', 'header', 'keywords', 'description', 'intro', 'text']

translator.register(Page, PageTranslationOptions)


class MediaTranslationOptions(TranslationOptions):
	fields = ['name', 'description']

translator.register(Media, MediaTranslationOptions)
