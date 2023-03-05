from django.urls import path
from .views import users, register, login, AuthenticatedUser

urlpatterns = [
    path('users/all', users),
    path('users/reg', register),
    path('users/login', login),
    path('users/user', AuthenticatedUser.as_view())
]
