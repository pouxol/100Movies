from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
html = response.text

soup = BeautifulSoup(html, "html.parser")

movies = soup.find_all(name="h3", class_="title")

all_movies = []
for movie in movies:
    all_movies.append(movie.getText())

print(all_movies)
