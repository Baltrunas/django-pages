from django import template

from django.contrib.contenttypes.models import ContentType

from ..models import View


register = template.Library()


@register.simple_tag(takes_context=True)
def view(context, view_object, view=False):
	request = context.get('request')

	content_type = ContentType.objects.get_for_model(type(view_object))
	object_id = view_object.id

	if request.user.is_authenticated():
		user = request.user
	else:
		user = None

	if view:
		new_view = View(
			content_type=content_type,
			object_id=object_id,
			site=request.site,
			referer=request.META.get('HTTP_REFERER', ''),
			user_agent=request.META.get('HTTP_USER_AGENT', ''),
			ip=request.META.get('REMOTE_ADDR', ''),
			url=request.build_absolute_uri(),
			user=user
		)
		new_view.save()
	views = View.objects.filter(content_type=content_type, object_id=object_id)
	return views.count()
