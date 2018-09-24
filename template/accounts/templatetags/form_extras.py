from django import template

register = template.Library()


@register.inclusion_tag('registration/_form.html')
def form_tag(form, form_id, submit_label):
    return {
        'form': form,
        'form_id': form_id,
        'submit_label': submit_label
    }
