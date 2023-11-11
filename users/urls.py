from django.urls import path

from users.views import login, registration, get_all_users, get_user_by_id, create_user

app_name = 'users'

urlpatterns = [
    path('login/', login, name="login"),
    path('registration/', registration, name="registration"),
    path('get_all_users/', get_all_users, name="get_all_users"),
    path('get_user_by_id/', get_user_by_id, name="get_user_by_id"),
    path('get_user_by_id/', get_user_by_id, name="get_user_by_id"),
    path('create_user/', create_user, name="create_user"),
]