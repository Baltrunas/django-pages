from django import template
from django.utils.safestring import mark_safe

register = template.Library()


class RenderNode(template.Node):
	def __init__(self, content):
		self.content = content

	def render(self, context):
		try:
			self.content = template.resolve_variable(self.content, context)
			return template.Template(self.content).render(template.Context(context, autoescape=False))
		except template.TemplateSyntaxError as e:
			return mark_safe("<strong>Template error: There is an error one of this page's template tags: <code>%s</code></strong>" % e.message)


@register.tag(name='render')
def render(parser, token):
	'''
	Example: {% render content %}
	'''
	content = token.split_contents()[-1]
	return RenderNode(content)

render.is_safe = True
