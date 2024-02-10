import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)

app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key = 'jbdhzabibxsqnxq163878EYIAHaaonzs'
TOKEN_INFO = 'token_info'

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    #session.clear()
    #code = request.args.get('code')
    #token_info = create_spotify_oauth().get_access_token(code)
    #session[TOKEN_INFO] = token_info
    #return redirect(url_for('save_discover_weekly', external = True))
    session.clear()
    code = request.args.get('code')
    if code is None:
        return redirect(url_for('login'))

    try:
        token_info = create_spotify_oauth().get_access_token(code)
    except spotipy.oauth2.SpotifyOauthError as e:
        print("Error:", e)
        return redirect(url_for('login'))

    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_discover_weekly'))

@app.route('/saveInfo')
<<<<<<< HEAD
=======
def save_discover_weekly():
    try:
        token_info = get_token()
    except:
        print("User not logged int")
        return redirect('/')
    
    #return("OAUTH SUCCESSFUL")
    sp = spotipy.Spotify(auth=token_info['access_token'])
    user_id = sp.current_user()['id']
    saved_weekly_playlist_id = None
    discover_weekly_playlist_id = None

    current_playlists = sp.current_user_playlists()['items']
    
    for playlist in current_playlists:
        if(playlist['name'] == "Discover Weekly"):
            discover_weekly_playlist_id = playlist['id']
        if(playlist['name'] == "Saved Weekly"):
            saved_weekly_playlist_id = playlist['id']

    #if not discover_weekly_playlist_id:
        #return 'Discover Weekly not found'
    
    if not saved_weekly_playlist_id:
        new_playlist = sp.user_playlist_create(user_id, 'Saved Weekly', True)
        saved_weekly_playlist_id = new_playlist['id']

    discover_weekly_playlist = sp.playlist_items(discover_weekly_playlist_id)
    song_uris = []
    for song in discover_weekly_playlist['items']:
        song_uri = song['track']['uri']
        song_uris.append(song_uri)

    sp.user_playlist_add.tracks("Your User Id", saved_weekly_playlist_id, song_uris, None)
    return("Success !!!")

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', external=False))
        
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = '52e2918f1085491aa5b84ebe80a10cb3',
        client_secret = '2f03c93c756e440eb316e2a3c9c08876',
        redirect_uri = url_for('redirect_page', _external=True),
        scope = 'user-library-read playlist-modify-public playlist-modify-private'
    )

app.run(debug=True)
>>>>>>> cfdf0179c5f671837752003513d077e0fd50b7ca
