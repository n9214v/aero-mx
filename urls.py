"""Aero-MX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from aero_mx.views import general_views, hangar_views

general_paths = [
    path('', general_views.home, name='home'),
]

hangar_paths = [
    path('', hangar_views.home, name='home'),
    path('aircraft/add', hangar_views.add_aircraft, name='add_aircraft'),

]

urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path('^accounts/', include('allauth.urls')),
    re_path('^base/', include(('mjg_base.urls', 'mjg_base'), namespace='base')),
    re_path('^hangar/', include((hangar_paths, 'aero_mx'), namespace='hangar')),
    re_path('', include((general_paths, 'aero_mx'), namespace='aero')),
]
