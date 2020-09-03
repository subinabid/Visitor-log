from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from core import views

urlpatterns = [
    path('',                TemplateView.as_view(template_name = "home.html"),  name = "home"),
    path('visitors/',       views.visitors,                                     name = "visitors"),
    path('visitors/add',    views.visitors_add,                                 name = "visitors_add"),
    path('admin/',      admin.site.urls),
    path('accounts/',   include('django.contrib.auth.urls')),
]