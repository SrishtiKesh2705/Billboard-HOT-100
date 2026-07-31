from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
SPOTIFY_ENDPOINT="https://api.spotify.com/v1/me/playlists"
parameters={
    "name": "Billboard HOT 100",
    "description": "Billboard HOT 100 songs on the date entered by the user",
    "public": False
}

date=input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD:")
url="https://www.billboard.com/charts/hot-100/"+date
headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36"
}
response=requests.get(url=url,headers=headers)
billboard_web_page=response.text
soup=BeautifulSoup(billboard_web_page,"html.parser")
songs=soup.find_all(name="h3",class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")
song_list=[song.getText(strip=True) for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        redirect_uri=os.environ["SPOTIFY_REDIRECT_URI"],
        scope="playlist-modify-private",
        cache_path="token.txt",
        username="somixan"
    )
)

user_id = sp.current_user()["id"]

song_uri_list= []
for song in song_list:
    result = sp.search(q=f"track:{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.current_user_playlist_create(f"{date} Billboard HOT 100",public=False,collaborative=False,description="Created using the spotify API")
sp.playlist_add_items("5CJP9k8EzhvvQL2TnTJIxP",items=song_uri_list)