from django import template

register = template.Library()


@register.inclusion_tag('registration/_form.html')
def form_tag(form_id, form):
    return {
        'form_id': form_id,
        'form': form
    }
