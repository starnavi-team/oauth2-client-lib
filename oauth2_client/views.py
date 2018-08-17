import requests
from django.conf import settings
from django.http import HttpResponse
from django.views import View


class OAuth2Callback(View):
    def get(self, request):
        url = f'{settings.OAUTH2_SERVER}/token/'
        data = {
            'grant_type': 'authorization_code',
            'code': request.GET.get('code'),
            'client_id': settings.OAUTH2_CLIENT_ID,
            'client_secret': settings.OAUTH2_CLIENT_SECRET,
            'redirect_uri': settings.OAUTH2_CLIENT_REDIRECT_URI,
        }
        response = requests.post(url, data=data)
        return HttpResponse(response.text)
