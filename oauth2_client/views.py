import urllib

import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.generic import View, RedirectView


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

        redirect_uri = request.GET.get('state', '/') + '?' + \
                       urllib.parse.urlencode(response.json())
        return redirect(redirect_uri)


class OAuth2Login(RedirectView):
    def get_redirect_url(self):
        url = f'{settings.OAUTH2_SERVER}/authorize/'
        client_id = settings.OAUTH2_CLIENT_ID
        redirect_uri = self.request.META.get("HTTP_REFERER", '/').split('?')[0]

        return f'{url}?response_type=code&client_id={client_id}&state={redirect_uri}'


class OAuth2Logout(View):
    def get(self, request):
        if 'token' in request.GET:
            url = f'{settings.OAUTH2_SERVER}/revoke_token/'
            token = request.GET['token']
            data = {
                'token': token,
                'client_id': settings.OAUTH2_CLIENT_ID,
                'client_secret': settings.OAUTH2_CLIENT_SECRET,
            }
            response = requests.post(url, data=data)

            redirect_uri = self.request.META.get("HTTP_REFERER", '/').split('?')[0]
            return redirect(redirect_uri)

        return HttpResponseBadRequest('Token is not provided')


class OAuth2Refresh(View):
    def get(self, request):
        if 'refresh_token' in request.GET:
            url = f'{settings.OAUTH2_SERVER}/token/'
            refresh_token = request.GET['refresh_token']
            data = {
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token,
                'client_id': settings.OAUTH2_CLIENT_ID,
                'client_secret': settings.OAUTH2_CLIENT_SECRET,
            }
            response = requests.post(url, data=data)

            redirect_uri = self.request.META.get("HTTP_REFERER", '/').split('?')[0] + '?' + \
                           urllib.parse.urlencode(response.json())
            return redirect(redirect_uri)

        return HttpResponseBadRequest('Refresh token is not provided')
