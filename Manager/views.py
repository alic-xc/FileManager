from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import folderForm
from .models import *

import os

# Create your views here.



def homepage(request):

    return render(request, "Manager/app/homepage.html", )


def directory(request):



    if request.method == 'POST':

        folder_form = folderForm(request.POST)

        if folder_form.is_valid():

            try:
                #checking database for existing name

                exist = Folder.objects.filter(name=folder_form.cleaned_data['folder_name'])
                if len(exist) > 0 :
                    raise Exception("Name already exist")

                # setting creating a custom folder to media
                if os.path.exists(f"media/{ folder_form.cleaned_data['folder_name'] }") :
                    raise Exception("Folder already exist !")

                os.mkdir(f"media/{folder_form.cleaned_data['folder_name']}")

                folder = Folder(name=folder_form.cleaned_data['folder_name'],
                                hidden=folder_form.cleaned_data['status'])

                folder.save()

                messages.success(request, "Folder created successfully")


                # folder = Folder(name)

            except Exception as err:
                messages.error(request,err)

            return HttpResponseRedirect(reverse("folder"))

    context = {
        'recently': Folder.custom.created_recently(),
        'directories': Folder.objects.all(),
        'form': folderForm()
    }
    return render(request, "Manager/app/folder.html", context=context)


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

