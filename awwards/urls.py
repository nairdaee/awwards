from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views 
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
