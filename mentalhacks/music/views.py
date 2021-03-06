from django.shortcuts import render

# Create your views here.
import requests
import unicodedata
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import requests
import urllib
import json 
from pprint import pprint

from .models import Journal
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="6d2b2b6bc36648b6a1667d90b4415832",
                                                           client_secret="a06408476f1b453b89fba8608604ce0d"))

def index(request):
    return render(request, "Home-Page.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contact(request):
    return render(request, "Contact-Us.html")

def services(request):
    return render(request, "Services.html")

def pacman(request):
    return render(request, "pacman.html")

def songsuggestion(request):
    playlist_id = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJiZcmkrIHGU'
    # spotify:playlist:37i9dQZF1DWU0ScTcjJBdj
    results = sp.playlist(playlist_id)
    # print(json.dumps(results, indent=4))
    # print("2")
    result = []
    for idx, track in enumerate(results['tracks']['items']):
        # print( track['track']['external_urls'])  #url of song
        # print( track['track']['name']) #name of song
        # print( json.dumps(track['track']['album']['images'][0]['url'], indent=4)) #image
        # print( json.dumps(track['track']['album']['artists'][0]['external_urls']['spotify'], indent=4))  #artist url
        # print( json.dumps(track['track']['album']['artists'][0]["name"], indent=4))  #artist name
        print( json.dumps(track['track']['album']['artists'][0]["name"], indent=4))
        temp = {}

        temp['title'] = track['track']['name']
        temp['image'] = track['track']['album']['images'][0]['url']
        temp['artists'] = track['track']['album']['artists'][0]["name"]
        temp['artist_url'] = track['track']['album']['artists'][0]['external_urls']['spotify']
        temp['songURL'] = track['track']['external_urls']['spotify']
        
        result.append(temp)
        
    print(result)    

    return render(request, "songsuggestion.html", {"musicData":result})   


def diary(request):
    if request.method== 'POST':
        title = request.POST['entry-title']
        content = request.POST['daily-entry']
        print(title)
        print(content)

        Journal.objects.create(user = request.user, title=title, content=content)
    
    return render(request, "diary.html")

def meditation(request):
    return render(request, "meditation.html")

def color_game(request):
    return render(request, "color_index.html")

def diary_list(request):

    data = Journal.objects.filter(user = request.user)
    return render(request, "diary_list.html", {"data":data})   

def diary_single(request, id):
    print(id)
    data = Journal.objects.get(id = id)
    print(data.content)
    return render(request, "diary_single.html", {"data":data})
    
# import spotipy


# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="6d2b2b6bc36648b6a1667d90b4415832",
#                                                            client_secret="a06408476f1b453b89fba8608604ce0d"))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])    