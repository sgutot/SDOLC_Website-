from django import template

register = template.Library()

@register.filter
def get_field(form, field_name):
    return form[field_name]

@register.filter
def get_field_verbose_name(form, prefix):
    # This is a simplified version - you'll need to implement this based on your actual field names
    fields = {
        'sqd1': 'Time spent for transaction was acceptable',
        'sqd2': 'Requirements and steps were clear',
        'sqd3': 'Staff were competent and knowledgeable',
        'sqd4': 'Staff were courteous and approachable',
        'sqd5': 'Facilities were adequate and comfortable',
        'sqd6': 'Overall satisfaction with the service',
        'sqd7': 'Would recommend this office to others',
        'sqd8': 'The service met my expectations',
    }
    return fields.get(prefix, '')