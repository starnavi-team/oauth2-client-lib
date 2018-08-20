import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse
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
        return JsonResponse(response.json())


class OAuth2Login(RedirectView):
    def get_redirect_url(self):
        url = f'{settings.OAUTH2_SERVER}/authorize/'
        client_id = settings.OAUTH2_CLIENT_ID

        return f'{url}?response_type=code&client_id={client_id}'


class OAuth2Logout(View):
    def get(self, request):
        if token in request.GET:
            url = f'{settings.OAUTH2_SERVER}/revoke_token/'
            token = request.GET['token']
            data = {
                'token': token,
                'client_id': settings.OAUTH2_CLIENT_ID,
                'client_secret': settings.OAUTH2_CLIENT_SECRET,
            }
            response = requests.post(url, data=data)
            return HttpResponse(response.text)
        else:
            return HttpResponse('Token is not provided')
