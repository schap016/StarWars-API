import swapi.models
import requests


response = requests.get("https://swapi.co/api/films/6")
raw_data = response.text
film_obj = swapi.models.Film(raw_data)

print(film_obj.get_characters())