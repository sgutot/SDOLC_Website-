from django import template

register = template.Library()

@register.filter(name='get_field')
def get_field(form, field_name):
    """Get form field by name"""
    return form[field_name]

@register.filter(name='get_field_label')
def get_field_label(field):
    """Get field label"""
    return field.field.label