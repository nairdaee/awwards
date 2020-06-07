from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url(r'^myprofile$',views.profile,name='myprofile'),
    url(r'^profile/edit$',views.edit_profile,name='edit'),
    url(r'^project/new$', views.new_project, name='post'),
    url(r'^project/(?P<project_id>[0-9])$',views.project,name='project'),
    url(r'^search/', views.search,name='search'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'api/projects/project-id/(?P<pk>[0-9]+)/$', views.ProjectDescription.as_view()),
    url(r'api/profiles/profile-id/(?P<pk>[0-9]+)/$', views.ProfileDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)