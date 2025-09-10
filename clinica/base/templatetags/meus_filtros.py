from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter
def format_cpf(value):
    value = ''.join(filter(str.isdigit, str(value)))
    if len(value) == 11:
        return f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}"
    return value
