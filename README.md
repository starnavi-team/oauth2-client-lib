# Django OAuth2 client
## Quick start
Add **oauth2_client** to your INSTALLED_APPS settings:
```
INSTALLED_APPS = [
    ...
    'oauth2_client',
]
```
Include **oauth2_client.urls** in your project urls.py:
```
path('', include('oauth2_client.urls')),
```
Add variables to settings:
```
OAUTH2_SERVER = '<server_addess>'
OAUTH2_CLIENT_ID = '<application's id>'
OAUTH2_CLIENT_SECRET = '<application's secret>'
LOGIN_REDIRECT_URL = '/'
```
Add to template:
```
{% load oauth2_client %}
...
<a href="{% oauth2_url %}">Log in</a>
```
After success login, token is stored in session:
``request.session['access_token']``