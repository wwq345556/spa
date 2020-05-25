"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from flora import views
from django.urls import include,path
import base
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import handler404
# from django.http import Http404

urlpatterns = [
    url(r'^media/(?P<path>.*)',serve,{"document_root":settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('index',views.hello),
    path('flora/',include('flora.urls')),
    path('plants/',include('plants.urls'))
]
# urlpatterns += staticfiles_urlpatterns()
# handler400 = views.bad_request
# handler403 = views.permission_denied
# handler404 = base.common.page_not_found()
# handler500 = views.page_error