from flask import Flask, render_template, request, redirect, url_for
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import pprint
import flask_bootstrap
from keys import *
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENTID,
                                               client_secret=CLIENTSECRET,
                                               redirect_uri=SIU,
                                               scope=SCOPE))
app = Flask(__name__)
flask_bootstrap.Bootstrap(app)

@app.route('/')
def index():
    # get the song that the user is listening to
    current_song = sp.current_user_playing_track()
    playlists = []
    #get user id
    user = sp.current_user()
    #get user's playlists
    x = sp.user_playlists(user['id'])
    for i in x['items']:
        playlists.append(i)
    #get user's top tracks
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')
    #get user's top artists
    pprint.pprint(current_song)
    return render_template('index.html', playlists=playlists, top_tracks=top_tracks,current_song=current_song)

app.run(debug=True)