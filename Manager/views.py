from django.shortcuts import render
from django.http import HttpResponse
from .models import *

import os

# Create your views here.



def homepage(request):

    context = {
        'folder': Folder.custom.created_recently(),
        'videos': Videos.custom.created_recently(),
        'pictures': Pictures.custom.created_recently(),
        'audio': Audio.custom.created_recently(),
        'document': Document.custom.created_recently()
    }

    return render(request, "Manager/app/homepage.html", context=context)


def directory(request):
    pass

def view_directory(request, folder):
    pass

def video(request):
    pass


def play_video(request, filename):
    pass

def audio(request):
    pass

def play_audio(request, filename):
    pass

def picture(request):
    pass

def view_picture(request, filename):
    pass

def document(request):
    pass

def view_document(request, filename):
    pass

