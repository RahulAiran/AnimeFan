from django.urls import path, register_converter

from . import converters, views
from django.contrib import admin 
from django.urls import path, include 
from django.conf.urls import url 
from animefan.views import *

register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [ 
    path('', views.index, name='index'),
    path('<int:anime_id>/', views.detailanimeid, name='detail'),
    path('name-<str:name>/', views.detailname, name='detail'),
    path('mood-<str:mood>-<int:number>/', views.detailmood, name='detail'),
    path('rating-<float:rating>/', views.detailrating, name='detail'),
    path('rating-<int:rating>/', views.detailrating, name='detail'),
]