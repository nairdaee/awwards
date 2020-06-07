from django.conf.urls import url,include
from django.contrib import admin
from rating import views
from django.contrib.auth import views 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('rating.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^api-token-auth/', obtain_auth_token) 
]
