"""CryptoPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from dash.apis import ChartData, SpotData, CMCData

urlpatterns = [
    path('', include('dash.urls')),
    path('admin/', admin.site.urls),
    path('signup/', include('profilemanager.urls')),
    url(r'^login/$', login, {'template_name': 'profilemanager/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'profilemanager/logout.html'}),
    url(r'^api/data/chart/$', ChartData.as_view(), name='api-chart-data'),
    url(r'^api/data/spot/$', SpotData.as_view(), name='api-spot-data'),
    url(r'^api/data/cmc/$', CMCData.as_view(), name='api-cmc-data'),
    url(r'^chat/', include('chat.urls')),
]
