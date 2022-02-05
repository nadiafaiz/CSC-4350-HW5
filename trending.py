import requests
import os
from dotenv import find_dotenv, load_dotenv

def get_trending_movies():
    load_dotenv(find_dotenv())

    API_KEY = os.getenv("API_KEY")
    TRENDING_URL = "https://api.themoviedb.org/3/trending/all/day?api_key=" + API_KEY

    response = requests.get(TRENDING_URL)

    response_json = response.json()

    try:
        movies = response_json["results"]
        filtered_movies = filter(titled_movies, movies)

        for movie in filtered_movies:
            print(movie["original_title"])
    except KeyError:
        print("Couldn't fetch movies!")

def titled_movies(movie):
    return "original_title" in movie

get_trending_movies()