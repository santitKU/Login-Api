from django.contrib import admin
from django.urls import path, include
from user_handeling.views import LoginAPI
from knox import views as knox_views

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("api/login/", knox_views.LogoutView.as_view(), name='login'),
    path("api/logout/", knox_views.LogoutView.as_view(), name = 'logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]