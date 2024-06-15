"""chruutundruebli URL Configuration

The `urlpatterns` list routes URLs to views. 
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
from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
import juntagrico
from chruutundruebli import views as cviews
from dbexport import views as dbexportviews

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('juntagrico.urls')),
    re_path(r'^', include('juntagrico_pg.urls')),
    re_path(r'^impersonate/', include('impersonate.urls')),

    #export
    path('my/export/subscriptions', cviews.excel_export_subscriptions, name='export-subscriptions'),
    path('my/export/db-export', dbexportviews.db_export, name='export-db'),
    path('my/export/db-export-generate', dbexportviews.db_export_generate, name='generate-export-db')
]
