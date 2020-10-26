# from django.http import request
from pdb import set_trace
from django.db.models import query
from django.http import response
from django.shortcuts import render
from django.core.paginator import Paginator
# from django.http import HttpResponse
# import requests
from django.http import JsonResponse
from django.views.generic import View
from requests.api import options, request

from .models import Anime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def tribute(request):
    return render(request, 'tribute.html')

class search(View):
    # model = Anime
    template_name = "search.html"

    def get(self, request):
        return render(request, self.template_name, {'hidden': True, 'query': 'NULL'})

    def post(self, request):
        # import pdb; pdb.set_trace()
        query = self.request.POST.get('searchbar', None)
        response = detailname(request, query, 'WEB')

        if query == "":
            return render(request, self.template_name, {'hidden': True, 'no_search': True, 'query': 'NULL'})
        else:
            return render(request, self.template_name, {'response': response, 'hidden': False, 'query': query})

class popularity(View):
    template_name = "search.html"

    def get(self, request):
        # import pdb; pdb.set_trace()
        tmpresponse = detailpopularity(request, 'WEB')
        
        paginator = Paginator(tmpresponse, 30)
        page_number = request.GET.get('page')
        response = paginator.get_page(page_number)

        return render(request, self.template_name, {'response': response, 'hidden': False, 'query': 'NULL'})

class rating(View):
    template_name = "search.html"

    def get(self, request):
        tmpresponse = toprated(request, 'WEB')
        paginator = Paginator(tmpresponse, 30)
        page_number = request.GET.get('page')
        response = paginator.get_page(page_number)

        return render(request, self.template_name, {'response': response, 'hidden': False, 'query': 'NULL'})

class mood(View):
    template_name = "search.html"

    def get(self, request, mood):
        tmpresponse = detailmood(request, mood, 'WEB')
        paginator = Paginator(tmpresponse, 30)
        page_number = request.GET.get('page')
        response = paginator.get_page(page_number)

        return render(request, self.template_name, {'response': response, 'hidden': False, 'query': 'NULL'})

class genre(View):
    template_name = "search.html"

    def get(self, request, genre):
        tmpresponse = detailgenre(request, genre, 'WEB')
        paginator = Paginator(tmpresponse, 30)
        page_number = request.GET.get('page')
        response = paginator.get_page(page_number)

        return render(request, self.template_name, {'response': response, 'hidden': False, 'query': 'NULL'})

def detailanimeid(request, anime_id, options='NULL'):
    i = 0
    anime = Anime.objects.get(anime_id = int(anime_id))
    response = {
        'SNo' : i+1,
        'AnimeID' : anime.anime_id,
        'AnimeName' :  anime.name,
        'Genre' : anime.genre, 
        'AnimeType' : anime.animetype,
        'Episodes' : anime.episodes,
        'Rating' : anime.rating,
        'Members' : anime.members,
        'Mood': anime.mood
    }
    # return response
    if options == 'NULL':
        return JsonResponse(response, safe=False)
    else:
        return response
    
    # return HttpResponse("You're looking at mood : %s" %anime.mood ) 

def detailname(request, name, options='NULL'):
    i = 0
    result = []
    name = name.title()
    animes = Anime.objects.filter(name__contains = name)

    # response = [{} for x in range(len(anime))]

    # while i < len(anime):
    for anime in animes:
        response = {
            'SNo' : i+1,
            'AnimeID' : anime.anime_id,
            'AnimeName' :  anime.name,
            'Genre' : anime.genre, 
            'AnimeType' : anime.animetype,
            'Episodes' : anime.episodes,
            'Rating' : anime.rating,
            'Members' : anime.members,
            'Mood': anime.mood
        }
        i+=1
        result.append(response)
    
    # return result
    if options == 'NULL':
        return JsonResponse(result, safe=False)
    else:
        return result

def detailmood(request, mood, options='NULL'):
    i = 0
    result = []
    mood = mood.title()
    animes = Anime.objects.filter(mood = mood)
    
    for anime in animes:
        response = {
            'SNo' : i+1,
            'AnimeID' : anime.anime_id,
            'AnimeName' :  anime.name,
            'Genre' : anime.genre, 
            'AnimeType' : anime.animetype,
            'Episodes' : anime.episodes,
            'Rating' : anime.rating,
            'Members' : anime.members,
            'Mood': anime.mood
        }
        i+=1
        result.append(response) 

    if options == 'NULL':
        return JsonResponse(result, safe=False)
    else:
        return result

def detailrating(request, rating, options='NULL'):
    i = 0
    result = []
    animes = Anime.objects.filter(rating__gte = rating)
    
    for anime in animes:
        response = {
            'SNo' : i+1,
            'AnimeID' : anime.anime_id,
            'AnimeName' :  anime.name,
            'Genre' : anime.genre, 
            'AnimeType' : anime.animetype,
            'Episodes' : anime.episodes,
            'Rating' : anime.rating,
            'Members' : anime.members,
            'Mood': anime.mood
        }
        i+=1
        result.append(response) 

    if options == 'NULL':
        return JsonResponse(result, safe=False)
    else:
        return result

def toprated(request, options='NULL'):
    i = 0
    result = []
    animes = Anime.objects.order_by('-rating')
    
    for anime in animes:
        response = {
            'SNo' : i+1,
            'AnimeID' : anime.anime_id,
            'AnimeName' :  anime.name,
            'Genre' : anime.genre, 
            'AnimeType' : anime.animetype,
            'Episodes' : anime.episodes,
            'Rating' : anime.rating,
            'Members' : anime.members,
            'Mood': anime.mood
        }
        i+=1
        result.append(response) 

    if options == 'NULL':
        return JsonResponse(result, safe=False)
    else:
        return result

def detailpopularity(request, options='NULL'):
    i = 0
    result = []
    animes = Anime.objects.order_by('-members')
    
    for anime in animes:
        response = {
            'SNo' : i+1,
            'AnimeID' : anime.anime_id,
            'AnimeName' :  anime.name,
            'Genre' : anime.genre, 
            'AnimeType' : anime.animetype,
            'Episodes' : anime.episodes,
            'Rating' : anime.rating,
            'Members' : anime.members,
            'Mood': anime.mood
        }
        i+=1
        result.append(response) 

    if options == 'NULL':
        return JsonResponse(result, safe=False)
    else:
        return result

def detailgenre(request, genre, options='NULL'):
    i = 0
    result = []
    genre = genre.title()
    animes = Anime.objects.filter(genre__contains = genre)
    
    for anime in animes:
        response = {
            'SNo' : i+1,
            'AnimeID' : anime.anime_id,
            'AnimeName' :  anime.name,
            'Genre' : anime.genre, 
            'AnimeType' : anime.animetype,
            'Episodes' : anime.episodes,
            'Rating' : anime.rating,
            'Members' : anime.members,
            'Mood': anime.mood
        }
        i+=1
        result.append(response) 

    if options == 'NULL':
        return JsonResponse(result, safe=False)
    else:
        return result