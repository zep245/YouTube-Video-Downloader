from django import template

register = template.Library()

@register.filter
def kb_to_mb(value):
    if value:
        return round(value / 1024, 2)  # Convert KB to MB and round to 2 decimal places
    else:
        return 0  # Return 0 if value is empty or None
