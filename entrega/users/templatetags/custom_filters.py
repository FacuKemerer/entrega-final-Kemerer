from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def formato_tiempo(dt):
    diferencia = timedelta(hours=-3)
    hora_local = dt + diferencia

    formatted_date = hora_local.strftime("%d/%m/%Y")
    formatted_time = hora_local.strftime("%H:%M")
    return f"{formatted_date} {formatted_time}"



