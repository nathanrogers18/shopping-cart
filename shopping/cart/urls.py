from django.conf.urls import url
from . import views

app_name = 'cart'

urlpattern = [
    url(r'^index', views.IndexView.as_view(), name='index'),
]
