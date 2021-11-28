from django.shortcuts import render
from django.views.generic.base import View
from .models import *


class MovieView(View):
    def get(self, reqest):
        movies = Movie.objects.all()
        return render(reqest, 'movies/movies.html', {'movie_list': movies})

