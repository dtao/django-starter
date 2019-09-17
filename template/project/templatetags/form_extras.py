"""Template tags to assist in rendering forms."""

from django import forms
from django import template

register = template.Library()


@register.inclusion_tag('_form.html')
def form_tag(form, form_id, submit_label):
    """Render a <form> with the appropriate Bootstrap structure."""
    return {
        'form': form,
        'form_id': form_id,
        'submit_label': submit_label
    }


@register.filter
def is_textarea(field):
    """Indicate whether a field should be rendered as a <textarea>."""
    return isinstance(field.field.widget, forms.Textarea)


@register.filter
def field_value(field):
    """Provide a suitable field value defaulting to a blank string."""
    return field.value() or ''
