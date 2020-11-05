from django.contrib import admin
from .models import Category, MovieShots, Raiting, Reviews, RaitingStar, Movie, Genre, Actor

admin.site.register(Category)
admin.site.register(MovieShots)
admin.site.register(RaitingStar)
admin.site.register(Raiting)
admin.site.register(Reviews)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)



