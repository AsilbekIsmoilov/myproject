from django import template
import re
from ..models import Records

register = template.Library()

@register.filter
def get_dynamic_attr(obj, attr):
    return getattr(obj, attr, "")

@register.filter
def regex_search(value, pattern):
    match = re.search(pattern, value)
    if match:
        return match.group(1)
    return None

@register.filter
def get_record_by_code(records, call_code):
    return records.filter(call_code=call_code).first()


@register.filter
def split(value, delimiter=","):
    return value.split(delimiter)



@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
