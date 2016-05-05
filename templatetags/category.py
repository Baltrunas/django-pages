from django import template

from ..models import Page


register = template.Library()


def get_parent(page, level):
	if page.parent and page.level > level:
		return get_parent(page.parent, level)
	else:
		return page.parent

@register.simple_tag(takes_context=True)
def category(context, page, level=0, inc_last=True, tpl='pages/category.html'):
	parent = get_parent(page, level)

	context['level'] = 1
	context['pages'] = Page.objects.filter(parent=parent, public=True)
	context['inc_last'] = inc_last

	tpl = template.loader.get_template(tpl)
	return tpl.render(template.Context(context))
