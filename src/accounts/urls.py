from django.conf.urls import url

from . import views
from . import forms

# Стандартные вьюхи джанго
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^logout/$', auth_views.logout, name = 'logout'),
    url(r'^login/$', auth_views.login, name = 'login'),
    url(r'^signup/$', views.signup, name='signup'),
]

urlpatterns += [
    url(r'^profile/(?P<username>\w+)/$', views.profile, name = 'profile' )
]