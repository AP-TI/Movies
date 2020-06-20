from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    file = open(r'films\movies.txt')
    movies = file.readlines()
    return render(request, 'films/index.html', {'movies': movies})