"""polc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from .views import home, settings, password
from django.conf.urls import url, include
from django.contrib import admin




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^candidates/', include('candidateapp.urls', namespace='candidatesapp')),
    url(r'^$', home, name = 'home'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api/candidates/', include('candidateapp.api.urls', namespace='candiateapp-api')),
    url(r'^visualisation/', include('visualisation.urls', namespace='visualisation')),
    # url(r'^api/graph/', include('visualisation.api.urls', namespace='graph-api')),
]
