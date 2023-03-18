from django.urls import path
from . import views


app_name='basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'), # An empty string represents the root of this app. Pass a reference to index function. Don't call it with ().
    path('other/',views.other,name='other'),
]