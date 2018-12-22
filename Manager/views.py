from django.shortcuts import render
from django.http import HttpResponse
from .forms import folderForm
from .models import *

import os

# Create your views here.



def homepage(request):

    return render(request, "Manager/app/homepage.html", )


def directory(request):

    if request.method == 'GET':

        context = {
            'directories':Folder.custom.created_recently(),
            'form': folderForm()
        }
        return render(request, "Manager/app/folder.html", context = context)


    if request.method == 'POST':

        folder_form = folderForm(request.POST)

        if folder_form.is_valid():


            pass


        return HttpResponse("bad")

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

