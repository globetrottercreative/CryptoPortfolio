from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', login, {'template_name': 'profilemanager/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'profilemanager/logout.html'}),
]