from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("movies", views.movies),
    # * birinci slug tipi ikinci adı, movie_id yapabilirsin
    path("movies/<slug:slug>", views.movie_details),
]


