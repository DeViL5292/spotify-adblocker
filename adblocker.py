import os
import alsaaudio
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

# Spotify API credentials
SPOTIPY_CLIENT_ID = 'ced0076b536e435794381035fa15cd31'
SPOTIPY_CLIENT_SECRET = '4f5b0731e1dc4f36911072ddbb759a05'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Authenticate with Spotify API
scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Get system volume mixer
mixer = alsaaudio.Mixer()

def is_ad_playing():
    current_track = sp.current_playback()
    if current_track and current_track['currently_playing_type'] == 'ad':
        return True
    return False

def mute_volume():
    mixer.setvolume(0)
    print("Volume muted")

def unmute_volume():
    mixer.setvolume(50)  # Set to desired volume level
    print("Volume restored to normal")

try:
    print("Adblocker script started. Monitoring Spotify for ads...")
    ad_playing = False
    while True:
        if is_ad_playing():
            if not ad_playing:
                print("Ad detected! Muting volume...")
                mute_volume()
                ad_playing = True
        else:
            if ad_playing:
                print("No ad detected. Restoring volume...")
                unmute_volume()
                ad_playing = False
        sleep(5)  # Check every 5 seconds
except KeyboardInterrupt:
    print("Program stopped by user")
    unmute_volume()
