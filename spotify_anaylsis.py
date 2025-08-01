import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
results = sp.playlist_tracks(playlist_URI)

songs = []

# Loop through each track and collect data

for item in results['items']:
    track = item['track']
    track_id = track['id']

    audio_features = sp.audio_features(track_id)[0] if track_id else None
