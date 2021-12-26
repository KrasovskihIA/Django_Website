from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *
from .forms import ReviewForms
from django.db.models import Q


#Жанры и года выхода фильмов
class GenryYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MovieView(GenryYear, ListView):
    model= Movie
    queryset = Movie.objects.filter(draft=False)



class MovieDetailView(GenryYear, DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForms(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())



class ActorView(GenryYear, DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'



#Фильтры фильмов
class FilterMovieView(GenryYear, ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset