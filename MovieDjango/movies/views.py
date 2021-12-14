from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *
from .forms import ReviewForms


class MovieView(ListView):
    model= Movie
    queryset = Movie.objects.filter(draft=False)



class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForms(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())