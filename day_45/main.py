from os.path import exists
from bs4 import BeautifulSoup
import requests

if not exists("movies.txt"):
    response = requests.get(
        "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    )

    soup = BeautifulSoup(response.text, "html.parser")

    movie_title_tags = soup.select("h3.title")
    movie_titles_list = [item.getText() for item in movie_title_tags]
    movie_titles_list.reverse()

    with open("movies.txt", "a") as file:
        for movie_title in movie_titles_list:
            file.write(f"{movie_title}\n")
else:
    with open("movies.txt") as file:
        movie_titles = file.readlines()
        movie_titles_list = [item.replace("\n", "") for item in movie_titles]
