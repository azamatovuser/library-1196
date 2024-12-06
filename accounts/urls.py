from django.urls import path
from accounts.views import login_function, register_function


urlpatterns = [
    path('', login_function, name='login'),
    path('register/', register_function, name='register')
]