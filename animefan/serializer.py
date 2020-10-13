from rest_framework import serializers 
from . models import *
  
class ReactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Anime
        fields = ['anime_id','name', 'genre','animetype','episodes','rating','members','mood'] 