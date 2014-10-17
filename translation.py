# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from pages.models import Tag
from pages.models import Page

class TagTranslationOptions(TranslationOptions):
	fields = ['name']

translator.register(Tag, TagTranslationOptions)


class PageTranslationOptions(TranslationOptions):
	fields = ['title', 'header', 'keywords', 'description', 'intro', 'text']

translator.register(Page, PageTranslationOptions)
