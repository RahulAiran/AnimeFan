from animefan.views import search
from django.urls import path, register_converter

from . import converters, views
from django.conf.urls import url
from .views import genre, mood, search, popularity, rating

register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tribute/', views.tribute, name='tribute'),
    path('search/',  search.as_view(), name='search'),
    # url(r'^$', search.as_view(), name='search'),
    path('filter/popularity',  popularity.as_view(), name='popularity'),
    path('filter/rating', rating.as_view(), name='rating'),
    path('filter/mood-<str:mood>', mood.as_view(), name='mood'),
    path('filter/genre-<str:genre>', genre.as_view(), name='genre'),

    path('<int:anime_id>/', views.detailanimeid, name='JSON'),
    path('name-<str:name>/', views.detailname, name='JSON'),
    path('mood-<str:mood>', views.detailmood, name='JSON'),
    path('rating-<int:rating>/', views.detailrating, name='JSON'),
    path('rating-<float:rating>/', views.detailrating, name='JSON'),
    path('popularity', views.detailpopularity, name='JSON'),
    path('genre-<str:genre>', views.detailgenre, name='JSON'),
]