# Billboard-HOT-100
Scrapes Billboard Hot 100 songs for a selected date and creates a Spotify playlist using the Spotify Web API.

## 🚀 How It Works

1. The user enters a date.
2. The program sends a request to the Billboard Hot 100 website.
3. BeautifulSoup extracts the song titles from the chart.
4. Spotipy searches for each song on Spotify.
5. The songs are added to a new Spotify playlist.
6. The playlist is available in the user's Spotify account.

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup
- Spotipy
- Spotify Web API
- Python-dotenv

## 📂 Project Structure

```text
Spotify Playlist/
├── main.py
├── .env
├── .gitignore
└── README.md
