from django import template
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType


register = template.Library()


@register.tag
def edit_admin_link_for(parser, token):
    """
    Usage:
        1) load the templatetag: {% load editing_objects %};
        2) get the editing link of object: {% edit_admin_link_for object %}
    """
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, obj = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0])

    return EditObjectNode(obj)


class EditObjectNode(template.Node):
    def __init__(self, obj):
        self.obj = template.Variable(obj)

    def render(self, context):
        try:
            obj = self.obj.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        return get_edit_link(obj)


def get_edit_link(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    link = 'admin:%s_%s_change' % (content_type.app_label, content_type.model)
    return urlresolvers.reverse(link, args=(obj.id,))
