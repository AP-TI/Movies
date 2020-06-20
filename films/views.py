from django.core.serializers import json
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import dateformat
import datetime

import redis


redisClient = redis.Redis(host='localhost', port=6379, db=0)

# Create your views here.
def index(request):
    file = open(r'films\movies.txt')
    movies = file.readlines()
    if request.method == 'GET':
        return render(request, 'films/index.html', {'movies': movies})
    elif request.method == 'POST':
        search = request.POST["search"]
        redisClient.set('search:'+dateformat.format(datetime.datetime.now(), 'F j, Y, P'), search)
        results = []
        for movie in movies:
            if(search in movie):
                results.append(movie)
        return HttpResponse(results)

def search(request):
    return render(request, 'films/postMovie.html')