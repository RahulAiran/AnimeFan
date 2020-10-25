# from django.http import request
from pdb import set_trace
from django.http import response
from django.shortcuts import render
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
        return render(request, self.template_name, {'hidden': True})

    def post(self, request):
        # import pdb; pdb.set_trace()
        query = self.request.POST.get('searchbar', None)
        response = detailname(request, query, 'WEB')
        if query == "":
            return render(request, self.template_name, {'hidden': True, 'no_search': True})
        else:
            return render(request, self.template_name, {'response': response, 'hidden': False})

class popularity(View):
    template_name = "search.html"

    def get(self, request, number):
        # import pdb; pdb.set_trace()
        response = detailpopularity(request, number, 'WEB')
        return render(request, self.template_name, {'response': response, 'hidden': False})

class rating(View):
    template_name = "search.html"

    def get(self, request, number):
        response = toprated(request, number, 'WEB')
        return render(request, self.template_name, {'response': response, 'hidden': False})

class mood(View):
    template_name = "search.html"

    def get(self, request, mood, number):
        response = detailmood(request, mood, number, 'WEB')
        return render(request, self.template_name, {'response': response, 'hidden': False})

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

def detailname(request, name, options ='NULL'):
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

def detailmood(request, mood, number, options='NULL'):
    i = 0
    result = []
    number = (number-1) * 50
    mood = mood.title()
    animes = Anime.objects.filter(mood = mood)[number:number+50]
    
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

def detailrating(request, rating, number, options='NULL'):
    i = 0
    result = []
    number = (number-1) * 50
    animes = Anime.objects.filter(rating__gte = rating)[number:number+50]
    
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

def toprated(request, number, options='NULL'):
    i = 0
    result = []
    number = (number-1) * 50
    animes = Anime.objects.order_by('-rating')[number:number+50]
    
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

def detailpopularity(request, number, options='NULL'):
    i = 0
    result = []
    number = (number-1) * 50
    animes = Anime.objects.order_by('-members')[number:number+50]
    
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

def detailgenre(request, genre, number, options='NULL'):
    i = 0
    genre = genre.title()
    anime = Anime.objects.filter(genre = genre)
    response = [{} for x in range(number)]
    
    while i < number :
        response[i]["SNo"] = i+1
        response[i]["AnimeID"] = anime[i].anime_id
        response[i]["AnimeName"] = anime[i].name
        response[i]["Genre"] = anime[i].genre
        response[i]["AnimeType"] = anime[i].animetype
        response[i]["Episodes"] = anime[i].episodes
        response[i]["Rating"] = anime[i].rating
        response[i]["Members"] =  anime[i].members
        response[i]["Mood"] = anime[i].mood
        i += 1

    if options == 'NULL':
        return JsonResponse(response, safe=False)
    else:
        return render(request, "search.html", {'response': response, 'hidden': False})