from django.urls import path

from . import views

urlpatterns = [
    path('oauth2-callback/', views.OAuth2Callback.as_view()),
]
