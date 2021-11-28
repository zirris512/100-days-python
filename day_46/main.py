import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

scope = "playlist-modify-private"

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="https://example.com",
        scope=scope,
    )
)

user_id = spotify.current_user()["id"]

music_date = input("What year would you like to travel to? YYYY-MM-DD: ")

billboard_URL = f"https://www.billboard.com/charts/hot-100/{music_date}"
year = music_date.split("-")[0]

response = requests.get(billboard_URL)

soup = BeautifulSoup(response.text, "html.parser")

song_title_tags = soup.select("ul.o-chart-results-list-row h3#title-of-a-story")
song_titles = [item.getText().replace("\n", "") for item in song_title_tags]
song_uris = []

for track in song_titles:
    result = spotify.search(f"track: {track} year: {year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"'{track}' is unavailable on Spotify. Skipping...")

playlist = spotify.user_playlist_create(
    user=user_id, name=f"{music_date} Billboard 100", public=False
)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("\nSuccessfully added playlist.")
