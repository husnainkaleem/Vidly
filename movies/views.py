from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Movies
from django.shortcuts import render

# Create your views here.
def index(request):
    movies= Movies.objects.all()
    return render(request , 'movies/index.html', {'movies':movies})


def detail(request, movie_id):
    movie= get_object_or_404(Movies,pk=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})
