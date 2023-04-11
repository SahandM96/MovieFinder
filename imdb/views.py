import json
from json import JSONDecoder

from django.shortcuts import render
import requests

# Create your views here.
# API Key k_8f5dchwu
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36'}


@api_view(["GET"])
def search_movie_and_tv(request):
    url = "https://imdb-api.com/en/API/Search/k_12345678/" + request.GET.get(
        'name', '')
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def get_movie_tv_information(request):
    url = "https://imdb-api.com/en/API/Title/k_8f5dchwu/" + request.GET.get(
        'id', '') + "/FullActor,FullCast,Images,Ratings,"
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def get_top_250_movie(request):
    url = "https://imdb-api.com/en/API/Top250Movies/k_8f5dchwu"

    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def get_top_25_tv(request):
    url = "https://imdb-api.com/en/API/Top250TVs/k_8f5dchwu"
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def most_popular_movies(request):
    url = "https://imdb-api.com/en/API/MostPopularMovies/k_8f5dchwu"
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def most_popular_tv(request):
    url = "https://imdb-api.com/en/API/MostPopularTVs/k_8f5dchwu"
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def in_theaters(request):
    url = "https://imdb-api.com/en/API/InTheaters/k_8f5dchwu"
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def coming_soon(request):
    url = "https://imdb-api.com/en/API/ComingSoon/k_8f5dchwu"
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def box_office(request):
    url = "https://imdb-api.com/en/API/BoxOffice/k_8f5dchwu"
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def get_information_of_people(request):
    url = "https://imdb-api.com/en/API/Search/k_8f5dchwu/" + request.GET.get('id', '')
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response


@api_view(['GET'])
def get_awards_of_people(request):
    url = "https://imdb-api.com/en/API/NameAwards/k_8f5dchwu/" + request.GET.get('id', '')
    imdb_r = requests.get(url=url, headers=headers)
    if imdb_r.status_code != 200:
        raise exceptions.NotFound("error on imdb api")
    dr = imdb_r.json()
    response = Response()
    response.data = dr
    return response
