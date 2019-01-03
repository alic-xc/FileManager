from django import forms
from .models import Folder


class FolderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=50,
                                  widget= forms.TextInput(
                                      attrs={'placeholder':'Type Folder Name Here','class':'form-control input-sm'}) )
    status = forms.ChoiceField(label='Status',
                               choices=(('','-- select folder attribute --'),(True, 'Hidden'),(False,'Unhide')),
                               widget= forms.Select(attrs={'class':'form-control input-sm'}),
                               )


class AudioForm(forms.Form):

    name = forms.CharField(label='Audio Name', max_length=50,
                                 widget=forms.TextInput(
                                   attrs={'placeholder':'Enter Name Here','class':'form-control input-sm','id':'audio'}))

    size = forms.IntegerField(
                              widget=forms.HiddenInput(
                                   attrs={'id':'size'})
                              )


    summary = forms.CharField(label='Audio Summary', max_length=200,
                              widget=forms.Textarea(
                                  attrs={'placeholder':'Enter Audio Summary','class':'form-control input-sm'}
                              ))
    folder = forms.ChoiceField(label='folder', choices=(Folder.objects.values('id','name')),
                               )

    folder = forms.ModelChoiceField(queryset=Folder.objects.all(), empty_label="--- select destination ---",
                                    widget=forms.Select(attrs={'class':'form-control input-sm'}))

    file = forms.FileField(label='Upload file',
                           widget=forms.FileInput(
                               attrs={'class':'form-control input-sm','id':'audio-file','accept':'.mp3,.wma,.wav'}))

class VideoForm():
    pass

class PictureForm():
    pass

class DocumentForm():
    pass