from django import template
from movies.models import Category, Movie

register = template.Library()

#Список всех категорий
@register.simple_tag()
def get_categories():
    return Category.objects.all()


#Список последних добавленных фильмов
@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by('id')[:count]
    return {'last_movies':movies}
