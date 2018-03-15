from django.conf.urls import url
from . import views
from profilemanager import views as pv

urlpatterns = [
    url(r'^$', views.home, name='homepage'),
    url(r'^editprofile/$', pv.editprofile, name='editprofile'),
]