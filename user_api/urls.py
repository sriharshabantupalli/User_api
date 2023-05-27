from django.urls import path
from .views import generate_access_token, insert_user_details, list_users

urlpatterns = [
    path('oauth/access-token/', generate_access_token, name='generate_access_token'),
    path('users/', list_users, name='list_users'),
    path('users/insert/', insert_user_details, name='insert_user_details'),
]