"""
URL configuration for Whisp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from feed import urls as feed_urls
from profiles import urls as profiles_urls
from notify import urls as notify_urls
from profiles.views import profile
from notify import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(feed_urls,namespace='feed')),
    path("profile/",include(profiles_urls,namespace='profiles')),
    path("profile/", profile, name="profile"),
    path('resetpassword/', views.reset_password,name='reset_password'),
    path("",include("allauth.urls")),
    path('notify/', include(notify_urls,namespace='notify')),   
    path('chat/',include('chat.urls')) 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
