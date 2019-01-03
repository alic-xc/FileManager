from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import FolderForm, AudioForm
from .models import *
from django.db import connection

#third party module
from pydub import AudioSegment
import os


# Create your views here.
def homepage(request):

    return render(request, "Manager/app/homepage.html" )


def directory(request):

    if request.method == 'POST':

        folder_form = FolderForm(request.POST)

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
            except Exception as err:
                messages.error(request,err)

            return HttpResponseRedirect(reverse("folder"))

    context = {
        'recently': Folder.custom.created_recently()[:3],
        'directories': Folder.objects.all(),
        'form': FolderForm()
    }
    return render(request, "Manager/app/folder.html", context=context)


def view_directory(request, folder):

    node = Folder.custom.get_all_files(folder)
    folder = Folder.objects.get(unique=folder)
    return render(request, 'Manager/app/view_folder.html', context={'directory':node,
                                                                    'name':folder.name,
                                                                    'video':['Mov','Avi','MP4'],
                                                                    'music':['MP3','WAV','WMA'],
                                                                    'document':['DOC','PDF'],
                                                                    'picture':['JPG','PNG','GIF']})


def audio(request):

    if request.method == 'POST':

        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():

            format = str(request.FILES['file']).rsplit(".")[-1]
            audio_tem = AudioSegment.from_file(request.FILES['file'],format=format)
            lenght = len(audio_tem) / 1000


            print(size)
            # pass

    context = {
        'music': Audio.objects.all(),
        'audio':AudioForm()
    }

    return render(request, "Manager/app/audio.html", context=context)

def play_audio(request, filename):
    pass

def video(request):
    pass


def play_video(request, filename):
    pass

def picture(request):
    pass

def view_picture(request, filename):
    pass

def document(request):
    pass

def view_document(request, filename):
    pass

