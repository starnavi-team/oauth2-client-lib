import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.views import View


class OAuth2Callback(View):
    def get(self, request):
        url = f'{settings.OAUTH2_SERVER}/token/'
        data = {
            'grant_type': 'authorization_code',
            'code': request.GET.get('code'),
            'client_id': settings.OAUTH2_CLIENT_ID,
            'client_secret': settings.OAUTH2_CLIENT_SECRET,
            'redirect_uri': request.build_absolute_uri(request.path),
        }
        response = requests.post(url, data=data)

        if response.ok:
            access_token = response.json().get('access_token')
            if access_token:
                request.session['access_token'] = access_token
                return redirect(settings.LOGIN_REDIRECT_URL)

        return HttpResponseForbidden()
