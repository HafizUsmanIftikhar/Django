from django.urls import path
from . import views


app_name='first_app'

urlpatterns=[
    path('register/',views.register,name='register'), # An empty string represents the root of this app. Pass a reference to index function. Don't call it with ().
    path('user_login/',views.user_login,name='user_login'),
]