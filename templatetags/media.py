from django import template
register = template.Library()

from ..models import Media


@register.simple_tag(takes_context=True)
def media_group(context, group, tpl='pages/__blocks/media.html', size=''):
	page = context['page']
	context['size'] = size
	context['media_group'] = Media.objects.filter(page=page, group=group, public=True)

	tpl = template.loader.get_template(tpl)
	return tpl.render(template.Context(context))
