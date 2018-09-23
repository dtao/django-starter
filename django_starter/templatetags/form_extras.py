from django import template

register = template.Library()


@register.inclusion_tag('registration/_field.html')
def field(form, field_name):
    return {
        'form': form,
        'field': form[field_name],
        'widget': form.fields[field_name].widget,
        'value': form[field_name].value() or ''
    }
