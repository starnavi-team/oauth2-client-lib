from django.urls import path

from . import views

app_name = 'oauth2_client'

urlpatterns = [
    path('callback/', views.OAuth2Callback.as_view(), name='callback'),
    path('login/', views.OAuth2Login.as_view(), name='login'),
    path('logout/', views.OAuth2Logout.as_view(), name='logout'),
]
