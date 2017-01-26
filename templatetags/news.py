from django import template

from ..models import Page


register = template.Library()


@register.simple_tag(takes_context=True)
def news(context, slug, order_by='created_at', tpl='pages/news.html'):

	context['news'] = Page.objects.filter(parent__slug=slug, public=True).order_by('created_at')

	tpl = template.loader.get_template(tpl)
	return tpl.render(template.Context(context))
