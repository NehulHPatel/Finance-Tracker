# authentication/urls.py

from django.urls import path
from .views import welcome, signup, login, base

urlpatterns = [
    path('', welcome, name='welcome'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('base/', base, name='base'),
]
