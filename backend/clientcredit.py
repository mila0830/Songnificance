from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from azapi import AZlyrics
from query import summarize_song
from lyrics import get_lyrics
from query import summarize_lyrics

#access to authorized tokens
load_dotenv()

client_id = os.getenv("CLIENT_ID_SPOT")
client_secret= os.getenv("CLIENT_SECRET_SPOT")

#function to get token to access spotify api
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url="https://accounts.spotify.com/api/token"
    headers = {
        #sending in authorization data
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type":"client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token=json_result["access_token"]
    return token

#needed for the following functions
def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

#function that gets all information on a top artist based on the artist name inputted
def search_for_artist(token, artist_name):
    url= "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    #query = f"q={artist_name}&type=artist,track"
    #limit 1 is the top artist
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url=url +query
    result = get(query_url, headers=headers)
    #json_result = json.loads(result.content)
    json_result = json.loads(result.content)["artists"]["items"]
    #print(json_result)
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    return json_result[0]

#function that gets all the songs of a certain artist given their ID
def get_songs_by_artist(token, artist_id):
    #want the top tracks of a specific artist -- need to have a country
    url= f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    
    json_result = json.loads(result.content)["tracks"]
    
    return json_result

#function that gets the information based on a track name given
def search_for_track(token, track_name):
    url= "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    #query = f"q={artist_name}&type=artist,track"
    #limit 1 is the top artist
    query = f"?q={track_name}&type=track&limit=1"

    query_url=url +query
    result = get(query_url, headers=headers)
    #json_result = json.loads(result.content)
    json_result = json.loads(result.content)["tracks"]["items"]
    
    if len(json_result) == 0:
        print("No track with this name exists...")
        return None
    return json_result[0]

#function that gets the year of a certain track given its ID
def get_year_of_track(token, track_id):
    #want the top tracks of a specific artist -- need to have a country
    url= f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    
    json_result = json.loads(result.content)['album']['release_date']
    
    return json_result

#function that gets year of a certain song given any track name inputted
def get_year_of_song(token, track):
    url= "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    #query = f"q={artist_name}&type=artist,track"
    #limit 1 is the top artist
    query = f"?q={track}&type=track&limit=1"

    query_url=url +query
    result = get(query_url, headers=headers)
    #json_result = json.loads(result.content)
    json_result = json.loads(result.content)["tracks"]["items"]
    
    if len(json_result) == 0:
        print("No track with this name exists...")
        return None
    track_id = json_result[0]["id"]
    url= f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    
    json_result = json.loads(result.content)['album']['release_date']
    
    return json_result

def get_summary_with_track_and_artist(token, track, artist):
    url= "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    #query = f"q={artist_name}&type=artist,track"
    #limit 1 is the top artist
    query = f"?q={track,artist}&type=track,artist&limit=1"

    query_url=url +query
    result = get(query_url, headers=headers)
    #json_result = json.loads(result.content)
    json_result = json.loads(result.content)["tracks"]["items"]
    
    if len(json_result) == 0:
        print("No track with this name exists...")
        return None
    track_id = json_result[0]["id"]
    url= f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    
    date = json.loads(result.content)['album']['release_date']
    year = int(date[0:4])
    if year < 2022:
        summary = summarize_song(artist, track, date)
        return summary
    else:
        lyrics = get_lyrics(artist, track)
        return summarize_lyrics(lyrics)


    
    

token = get_token()
result = search_for_artist(token, "The Backseat Lov")
result2 = search_for_track(token,"Firework")
track_id = result2["id"]
artist_id = result["id"]

songs = get_songs_by_artist(token, artist_id)
# print(get_year_of_track(token, track_id))
# print(get_year_of_song(token, "Firework"))
print(get_summary_with_track_and_artist(token, "yes, and?", "Ariana Grande"))


# for idx, song in enumerate(songs):
#     print(f"{idx+1}. {song['name']}")


