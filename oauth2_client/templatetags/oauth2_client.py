from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def oauth2_url():
    url = f'{settings.OAUTH2_SERVER}/authorize/'
    client_id = settings.OAUTH2_CLIENT_ID

    return f'{url}?response_type=code&client_id={client_id}'
