# Django OAuth2 client
## Quick start
Include **oauth2_client.urls** in your project urls.py:
```
path('oauth2/', include('oauth2_client.urls')),
```
Add variables to settings:
```
OAUTH2_SERVER = ''        # server address
OAUTH2_CLIENT_ID = ''     # application's id
OAUTH2_CLIENT_SECRET = '' # application's secret
```
Add to template:
```
<a href="{% url 'oauth2_client:login' %}">Log in</a>
<a href="{% url 'oauth2_client:logout' %}?token=<token>">Log out</a>
```