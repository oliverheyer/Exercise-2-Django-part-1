from django.db import models
from tastypie.resources import ModelResource, fields, ALL
from rental.models import Movie, Genre

# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = "movies"
        filtering = {
            'price': ALL,
            'title': ALL,
            'release_year':ALL
        }

     # check why order_by is not working
        ordering: ['release_year', 'price', 'title', 'director']


"""
Filtering:

?price=20

?price__gt=10
?price__lt=30

?title__contains=word
"""

