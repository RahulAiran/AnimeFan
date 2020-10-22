# from django.http import request
from django.shortcuts import render
# from django.http import HttpResponse
import requests
from django.http import JsonResponse
from django.views.generic import View

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
        return render(request, self.template_name)

    def post(self, request):
        query = self.request.POST.get('searchbar', None)
        # response = detailname(request, query)
        response = requests.get('http://127.0.0.1:8000/animefan/name-'+query).json()
        return render(request, self.template_name, {'response': response})

def detailanimeid(request, anime_id):
    i = 0
    anime = Anime.objects.get(anime_id = anime_id)

    response = [{}]

    response[i]["SNo"] = i+1
    response[i]["AnimeID"] = anime.anime_id
    response[i]["AnimeName"] = anime.name
    response[i]["Genre"] = anime.genre
    response[i]["AnimeType"] = anime.animetype
    response[i]["Episodes"] = anime.episodes
    response[i]["Rating"] = anime.rating
    response[i]["Members"] = anime.members
    response[i]["Mood"] = anime.mood

    return JsonResponse(response, safe=False)
    
    # return HttpResponse("You're looking at mood : %s" %anime.mood ) 

def detailname(request, name):
    i = 0
    name = name.title()
    anime = Anime.objects.filter(name__contains = name)

    response = [{} for x in range(len(anime))]

    while i < len(anime):
        response[i]["SNo"] = i+1
        response[i]["AnimeID"] = anime[i].anime_id
        response[i]["AnimeName"] = anime[i].name
        response[i]["Genre"] = anime[i].genre
        response[i]["AnimeType"] = anime[i].animetype
        response[i]["Episodes"] = anime[i].episodes
        response[i]["Rating"] = anime[i].rating
        response[i]["Members"] = anime[i].members
        response[i]["Mood"] = anime[i].mood
        i += 1

    return JsonResponse(response, safe=False)

def detailmood(request, mood, number):
    i = 0
    mood = mood.title()
    anime = Anime.objects.filter(mood = mood)
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

    return JsonResponse(response, safe=False)

def detailrating(request, rating):
    i = 0
    anime = Anime.objects.filter(rating__gte = rating)
    response = [{} for x in range(len(anime))]
    while i < len(anime) :
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

    return JsonResponse(response, safe=False)

def detailpopularity(request, number):
    i = 0
    number = number * 50
    anime = Anime.objects.order_by('-members')[number:number+50]
    response = [{} for x in range(len(anime))]
    while i < len(anime) :
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

    return JsonResponse(response, safe=False)

def detailgenre(request, genre, number):
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

    return JsonResponse(response, safe=False)