# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from pages.models import Tag
from pages.models import Page


def tag(request, slug):
	return render_to_response('pages/tag.html', context, context_instance=RequestContext(request))


def page(request, url):
	context = {}
	host = request.META.get('HTTP_HOST')

	page = get_object_or_404(Page, url=url, sites__domain__in=[host])
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description

	if page.template:
		template = page.template
	else:
		template = 'pages/default.html'

	# pages_list = Page.objects.filter(public=True, category__in=context['category'].get_all(), sites__domain__in=[host]).order_by('-created_at')
	# paginator = Paginator(pages_list, page.per_page)

	# page_number = request.GET.get('page')
	# try:
	# 	pages_list = paginator.page(page_number)
	# except PageNotAnInteger:
	# 	pages_list = paginator.page(1)
	# except EmptyPage:
	# 	pages_list = paginator.page(paginator.num_pages)

	# context['pages_list'] = pages_list

	return render_to_response(template, context, context_instance=RequestContext(request))
