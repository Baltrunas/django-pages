# -*- coding: utf-8 -*
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# from django.http import Http404
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Tag
from .models import Page


def tag(request, slug):
	context = {}
	host = request.META.get('HTTP_HOST')
	tag = get_object_or_404(Tag, slug=slug)
	context['tag'] = tag
	context['title'] = tag.name

	context['pages_list'] = Page.objects.filter(public=True, tags__slug__in=[slug], sites__domain__in=[host])

	return render(request, 'pages/tag.html', context)


def page(request, url):
	context = {}

	# Page
	host = request.META.get('HTTP_HOST')
	page = get_object_or_404(Page, url=url, sites__domain__in=[host])
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description

	# # Pagination
	# pages_list = Page.objects.filter(public=True, parent=page, sites__domain__in=[host])
	# page_number = request.GET.get('page', None)

	# paginator = Paginator(pages_list, page.per_page)
	# try:
	# 	pages_list = paginator.page(page_number)
	# except PageNotAnInteger:
	# 	pages_list = paginator.page(1)
	# except EmptyPage:
	# 	pages_list = paginator.page(paginator.num_pages)

	# context['pages_list'] = pages_list

	# Template
	if page.template:
		template = page.template
	else:
		template = 'pages/default.html'

	return render(request, template, context)
