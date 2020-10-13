from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

from .models import Anime

from django.shortcuts import render 
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from . serializer import *
# Create your views here. 
  
class ReactView(APIView): 
    
    serializer_class = ReactSerializer 
  
    # def get(self, request): 
    #     detail = [ {"name": detail.name,"detail": detail.detail}  
    #     for detail in Anime.objects.all()] 
    #     return Response(detail) 
  
    # def post(self, request): 
  
    #     serializer = ReactSerializer(data=request.data) 
    #     if serializer.is_valid(raise_exception=True): 
    #         serializer.save() 
    #         return  Response(serializer.data)
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the animefan index.")

def detailanimeid(request, anime_id):
    anime = Anime.objects.get(anime_id = anime_id)
    response = HttpResponse()

    response.write("Anime ID : %s <br>" % anime.anime_id)
    response.write("Anime Name : %s <br>" % anime.name)
    response.write("Genre : %s <br>" % anime.genre)
    response.write("Anime Type : %s <br>" % anime.animetype)
    response.write("Episodes : %s <br>" % anime.episodes)
    response.write("Rating : %s <br>" % anime.rating)
    response.write("Members : %s <br>" % anime.members)
    response.write("Mood : %s <br>" % anime.mood)

    return HttpResponse(response)

def detailname(request, name):
    i=0
    name=name.title()
    anime = Anime.objects.filter(name__contains = name)
    response = [{} for x in range(len(anime))]

    while i < len(anime):
        response[i]["S. No."] = i+1 
        response[i]["Anime ID"] = anime[i].anime_id
        response[i]["Anime Name"] = anime[i].name
        response[i]["Genre"] = anime[i].genre
        response[i]["Anime Type"] = anime[i].animetype
        response[i]["Episodes"] = anime[i].episodes
        response[i]["Rating"] = anime[i].rating
        response[i]["Members"] =  anime[i].members
        response[i]["Mood"] = anime[i].mood
        i+=1

    return JsonResponse(response, safe=False)



def detailmood(request, mood, number):
    i = 0
    mood = mood.title()
    anime = Anime.objects.filter(mood = mood)
    response = [{} for x in range(number)]
    while i < number :
        response[i]["S. No."] = i+1 
        response[i]["Anime ID"] = anime[i].anime_id
        response[i]["Anime Name"] = anime[i].name
        response[i]["Genre"] = anime[i].genre
        response[i]["Anime Type"] = anime[i].animetype
        response[i]["Episodes"] = anime[i].episodes
        response[i]["Rating"] = anime[i].rating
        response[i]["Members"] =  anime[i].members
        response[i]["Mood"] = anime[i].mood
        i += 1 

    return JsonResponse(response, safe=False)

def detailrating(request, rating):
    i=0
    #name=name.title()
    anime = Anime.objects.filter(rating__gte = rating)
    response = [{} for x in range(len(anime))]

    while i < len(anime):
        response[i]["S. No."] = i+1 
        response[i]["Anime ID"] = anime[i].anime_id
        response[i]["Anime Name"] = anime[i].name
        response[i]["Genre"] = anime[i].genre
        response[i]["Anime Type"] = anime[i].animetype
        response[i]["Episodes"] = anime[i].episodes
        response[i]["Rating"] = anime[i].rating
        response[i]["Members"] =  anime[i].members
        response[i]["Mood"] = anime[i].mood
        i+=1

    return JsonResponse(response, safe=False)