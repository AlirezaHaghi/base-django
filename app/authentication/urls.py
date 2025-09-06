from django.urls import path

from .views import api_login, api_logout, api_user_info

urlpatterns = [
    path("login/", api_login, name="api_login"),
    path("logout/", api_logout, name="api_logout"),
    path("user/", api_user_info, name="api_user_info"),
]

