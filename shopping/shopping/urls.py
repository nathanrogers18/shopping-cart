from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^cart', include('cart.urls')),
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
]
