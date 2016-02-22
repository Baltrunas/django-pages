from django import template
from django.template import Context
from django.template import Template

from ..models import Page
from ..models import Tag


register = template.Library()


@register.assignment_tag
def related(slug, limit=4):
	related_items = Page.objects.filter(public=True, tags__slug__in=[slug])[:limit]
	if not related_items:
		related_items = Page.objects.filter(public=True, main=True)[:limit]

	return related_items
