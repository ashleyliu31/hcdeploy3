from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter(needs_autoescape=True)
@stringfilter
def highlight(value, search_term, autoescape=True):
    # first compile the regex pattern using the search_term
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)

    # now replace
    new_value = pattern.sub('<span class="highlight">\g<0></span>', value)
    return mark_safe(new_value)

@register.filter(needs_autoescape=True)
@stringfilter
def show_excerpt(value, search_term, autoescape=True):
    match = re.search('.{0,300}' + re.escape(search_term) + '.{0,300}', str(value), re.IGNORECASE)
    if match: return mark_safe(match.group())
    return ''

