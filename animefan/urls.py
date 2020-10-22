from animefan.views import search
from django.urls import path, register_converter

from . import converters, views
from .views import search

register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tribute/', views.tribute, name='tribute'),
    path('search/',  search.as_view(), name='search'),
    path('<int:anime_id>/', views.detailanimeid, name='JSON'),
    path('name-<str:name>/', views.detailname, name='JSON'),
    path('mood-<str:mood>-<int:number>/', views.detailmood, name='JSON'),
    path('rating-<int:rating>/', views.detailrating, name='JSON'),
    path('rating-<float:rating>/', views.detailrating, name='JSON'),
    path('popularity-<int:number>/', views.detailpopularity, name='JSON'),
    path('genre-<str:genre>-<int:number>/', views.detailgenre, name='JSON'),
]