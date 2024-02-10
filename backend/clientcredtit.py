from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from azapi import AZlyrics

#access to authorized tokens
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret= os.getenv("CLIENT_SECRET")

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

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

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

#items contains all the different results


def get_songs_by_artist(token, artist_id):
    #want the top tracks of a specific artist -- need to have a country
    url= f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    
    return json_result

token = get_token()
result = search_for_artist(token, "The Backseat Lov")
artist_id = result["id"]

songs = get_songs_by_artist(token, artist_id)


for idx, song in enumerate(songs):
    print(f"{idx+1}. {song['name']}")

