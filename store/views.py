#from django.shortcuts import render
from django.http import HttpResponse

#from store.models import ALBUMS

# Create your views here.
"""def index(request):
    message = "Salut tous le monde"
    return HttpResponse(message)

def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = <ul>{}</ul>.format("\n".join(albums))
    return HttpResponse(message)


def detail(request, album_id):
    id = int(album_id)
    album = ALBUMS[id]
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = "Le nom de l'album est {}. il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)"""