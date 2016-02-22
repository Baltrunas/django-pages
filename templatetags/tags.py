from django import template
from django.template import Context
from django.template import Template

from ..models import Tag


register = template.Library()


@register.assignment_tag
def tags():
	tags = Tag.objects.all()
	return tags
