1. Add "oauth2_client" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'oauth2_client',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('', include('oauth2_client.urls')),

3. Add to settings::
    OAUTH2_SERVER - authorization server address
    OAUTH2_CLIENT_ID - application's id
    OAUTH2_CLIENT_SECRET - application's secret

4. Add to template:
  {% load oauth2_client %}
  ...
  <a href="{% oauth2_url %}">Log in</a>
