from django.urls import path
from .views import get_top_250_movie, search_movie_and_tv

urlpatterns = [
    path('top_250', get_top_250_movie),
    path('search_movie_and_tv', search_movie_and_tv)

]
