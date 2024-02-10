import spotipy
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)

app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key = 'jbdhzabibxsqnxq163878EYIAHaaonzs'
TOKEN_INFO = 'token_info'

@app.route('/')

@app.route('/redirect')

@app.route('/saveInfo')

