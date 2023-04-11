from django.urls import path
from .views import users, register, login, AuthenticatedUser, logout

urlpatterns = [
    path('users/all', users),
    path('users/reg', register),
    path('users/login', login),
    path('users/log_out', logout),
    path('users/user', AuthenticatedUser.as_view())
]
