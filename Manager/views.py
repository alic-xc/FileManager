from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from .models import *
from django.core.files.storage import FileSystemStorage
#third party module
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
                                                                    'video':['MOV','AVI','MP4'],
                                                                    'music':['MP3','WAV','WMA'],
                                                                    'document':['DOC','PDF'],
                                                                    'picture':['JPG','PNG','GIF']})


def audio(request):

    if request.method == 'POST':

        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            # import only on valid form input
            try:
                lists = ['mp3', 'wav', 'wma']

                al_ex = Audio.objects.filter(name= form.cleaned_data['name'])
                if al_ex.count() > 0:
                    raise Exception("Already Exist")

                ext = str(request.FILES['file']).rsplit(".")[-1]
                if ext  not in lists:
                    raise Exception('Not a valid type')

                folder = Folder.objects.get(pk=form.cleaned_data['folder'].id)
                file_name = f"{form.cleaned_data['name']}.{ext}"

                # saving to fs
                fs = FileSystemStorage('media/')
                fs.save(os.path.join(folder.name,file_name), request.FILES['file'])
                a = Audio(name=form.cleaned_data['name'],
                          format=ext.upper(),
                          size=form.cleaned_data['size'],
                          summary=form.cleaned_data['summary'],
                          folder=folder)

                # saving to model
                a.save()
                messages.success(request,'Data saved successfully')
                return HttpResponseRedirect(reverse('audio'))

            except ModuleNotFoundError:
                messages.error(request,'Server Internal Error!. Module Not Found')
                return HttpResponseRedirect(reverse('audio'))

            except Folder.DoesNotExist:

                messages.error(request,'Invalid Folder. Folder Not Found')
                return HttpResponseRedirect(reverse('audio'))

            except Exception as err:

                messages.error(request, err)
                return HttpResponseRedirect(reverse('audio'))

            # pass

    context = {
        'music': Audio.objects.all(),
        'recently':Audio.custom.created_recently(),
        'audio':AudioForm()
    }

    return render(request, "Manager/app/audio.html", context=context)


def play_audio(request, filename):

    try:
        node = Audio.objects.get(hash=filename)

        return render(request, 'Manager/app/view_audio.html', context={'music':node})

    except Audio.DoesNotExist:
        messages.error(request, "Music Not Found")
        return render(request, 'Manager/app/view_audio.html')

    except TypeError:

        messages.error(request, 'Needed a recognised Value')
        return render(request, 'Manager/app/view_audio.html')




def video(request):

    if request.method == 'POST':

        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                lists = ['mp4', 'avi', 'mov']

                al_ex = Videos.objects.filter(name= form.cleaned_data['name'])
                if al_ex.count() > 0:
                    raise Exception("Already Exist")

                ext = str(request.FILES['file']).rsplit(".")[-1]
                if ext  not in lists:
                    raise Exception('Not a valid type')

                folder = Folder.objects.get(pk=form.cleaned_data['folder'].id)
                file_name = f"{form.cleaned_data['name']}.{ext}"

                # saving to fs
                fs = FileSystemStorage('media/')
                a = Videos(name=form.cleaned_data['name'],
                          format=ext.upper(),
                          size=form.cleaned_data['size'],
                          summary=form.cleaned_data['summary'],
                          folder=folder)

                # saving to model
                a.save()
                fs.save(os.path.join(folder.name,file_name), request.FILES['file'])
                messages.success(request,'Data saved successfully')
                return HttpResponseRedirect(reverse('video'))

            except ModuleNotFoundError:
                messages.error(request,'Server Internal Error!. Module Not Found')
                return HttpResponseRedirect(reverse('video'))

            except Folder.DoesNotExist:

                messages.error(request,'Invalid Folder. Folder Not Found')
                return HttpResponseRedirect(reverse('video'))

            except Exception as err:

                messages.error(request, err)
                return HttpResponseRedirect(reverse('video'))

    context = {
        'recently': Videos.custom.created_recently(),
        'videos': Videos.objects.all(),
        'video': VideoForm()
    }

    return render(request, 'Manager/app/video.html', context=context)


def play_video(request, filename):
    try:
        node = Videos.objects.get(hash=filename)

        return render(request, 'Manager/app/view_video.html', context={'video':node})

    except Audio.DoesNotExist:
        messages.error(request, "Music Not Found")
        return render(request, 'Manager/app/view_video.html')

    except TypeError:

        messages.error(request, 'Needed a recognised Value')
        return render(request, 'Manager/app/view_video.html')

def picture(request):

    if request.method == 'POST':

        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                lists = ['jpg', 'png', 'gif']

                al_ex = Pictures.objects.filter(name= form.cleaned_data['name'])
                if al_ex.count() > 0:
                    raise Exception("Already Exist")

                ext = str(request.FILES['file']).rsplit(".")[-1]
                if ext  not in lists:
                    raise Exception('Not a valid type')

                folder = Folder.objects.get(pk=form.cleaned_data['folder'].id)
                file_name = f"{form.cleaned_data['name']}.{ext}"

                # saving to fs
                fs = FileSystemStorage('media/')
                a = Pictures(name=form.cleaned_data['name'],
                          format=ext.upper(),
                          size=form.cleaned_data['size'],
                          summary=form.cleaned_data['summary'],
                          folder=folder)

                # saving to model
                a.save()
                fs.save(os.path.join(folder.name,file_name), request.FILES['file'])
                messages.success(request,'Data saved successfully')
                return HttpResponseRedirect(reverse('picture'))

            except ModuleNotFoundError:
                messages.error(request,'Server Internal Error!. Module Not Found')
                return HttpResponseRedirect(reverse('picture'))

            except Folder.DoesNotExist:

                messages.error(request,'Invalid Folder. Folder Not Found')
                return HttpResponseRedirect(reverse('picture'))

            except Exception as err:

                messages.error(request, err)
                return HttpResponseRedirect(reverse('picture'))

    context = {
        'recently': Pictures.custom.created_recently(),
        'pictures': Pictures.objects.all(),
        'picture': PictureForm()
    }

    return render(request, 'Manager/app/pictures.html', context=context)


def view_picture(request, filename):
    pass

def document(request):
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                lists = ['doc', 'pdf']

                al_ex = Document.objects.filter(name= form.cleaned_data['name'])
                if al_ex.count() > 0:
                    raise Exception("Already Exist")

                ext = str(request.FILES['file']).rsplit(".")[-1]
                if ext  not in lists:
                    raise Exception('Not a valid type')

                folder = Folder.objects.get(pk=form.cleaned_data['folder'].id)
                file_name = f"{form.cleaned_data['name']}.{ext}"

                # saving to fs
                fs = FileSystemStorage('media/')
                a = Document(name=form.cleaned_data['name'],
                          format=ext.upper(),
                          size=form.cleaned_data['size'],
                          summary=form.cleaned_data['summary'],
                          folder=folder)

                # saving to model
                a.save()
                fs.save(os.path.join(folder.name,file_name), request.FILES['file'])
                messages.success(request,'Data saved successfully')
                return HttpResponseRedirect(reverse('document'))

            except ModuleNotFoundError:
                messages.error(request,'Server Internal Error!. Module Not Found')
                return HttpResponseRedirect(reverse('document'))

            except Folder.DoesNotExist:

                messages.error(request,'Invalid Folder. Folder Not Found')
                return HttpResponseRedirect(reverse('document'))

            except Exception as err:

                messages.error(request, err)
                return HttpResponseRedirect(reverse('document'))

    context = {
        'recently': Document.custom.created_recently(),
        'documents': Document.objects.all(),
        'document': DocumentForm()
    }

    return render(request, 'Manager/app/documents.html', context=context)

def view_document(request, filename):
    pass



#function without view
