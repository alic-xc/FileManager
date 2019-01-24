from django import forms
from .models import Folder


class FolderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=50,
                                  widget= forms.TextInput(
                                      attrs={'placeholder':'Type Folder Name Here','class':'form-control input-sm'}) )
    status = forms.ChoiceField(label='Status',
                               choices=(('','-- select folder attribute --'),(True, 'Private'),(False,'Public')),
                               widget= forms.Select(attrs={'class':'form-control input-sm'}),
                               )


class AudioForm(forms.Form):

    name = forms.CharField(label='Audio Name', max_length=50,
                                 widget=forms.TextInput(
                                   attrs={'placeholder':'Enter Name Here','class':'form-control input-sm','id':'audio'}))

    size = forms.IntegerField(
                              widget=forms.PrivateInput(
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

class VideoForm(forms.Form):
    name = forms.CharField(label='Video Name', max_length=50,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Enter Name Here', 'class': 'form-control input-sm',
                                      'id': 'audio'}))

    size = forms.IntegerField(
        widget=forms.PrivateInput(
            attrs={'id': 'size'})
    )

    summary = forms.CharField(label='Video Summary', max_length=200,
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'Enter Video Summary', 'class': 'form-control input-sm'}
                              ))
    folder = forms.ChoiceField(label='folder', choices=(Folder.objects.values('id', 'name')),
                               )

    folder = forms.ModelChoiceField(queryset=Folder.objects.all(), empty_label="--- select destination ---",
                                    widget=forms.Select(attrs={'class': 'form-control input-sm'}))

    file = forms.FileField(label='Upload file',
                           widget=forms.FileInput(
                               attrs={'class': 'form-control input-sm', 'id': 'video-file',
                                      'accept': '.mp4,.avi,.mov'}))

class PictureForm(forms.Form):
    name = forms.CharField(label='Picture Name', max_length=50,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Enter Name Here', 'class': 'form-control input-sm',
                                      'id': 'audio'}))

    size = forms.IntegerField(
        widget=forms.PrivateInput(
            attrs={'id': 'size'})
    )

    summary = forms.CharField(label='picture Summary', max_length=200,
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'Enter picture Summary', 'class': 'form-control input-sm'}
                              ))
    folder = forms.ChoiceField(label='folder', choices=(Folder.objects.values('id', 'name')),
                               )

    folder = forms.ModelChoiceField(queryset=Folder.objects.all(), empty_label="--- select destination ---",
                                    widget=forms.Select(attrs={'class': 'form-control input-sm'}))

    file = forms.FileField(label='Upload file',
                           widget=forms.FileInput(
                               attrs={'class': 'form-control input-sm', 'id': 'picture-file',
                                      'accept': '.jpg,.png,.gif'}))

class DocumentForm(forms.Form):
    name = forms.CharField(label='Document Name', max_length=50,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Enter Name Here', 'class': 'form-control input-sm',
                                      'id': 'audio'}))

    size = forms.IntegerField(
        widget=forms.PrivateInput(
            attrs={'id': 'size'})
    )

    summary = forms.CharField(label='Document Summary', max_length=200,
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'Enter document Summary', 'class': 'form-control input-sm'}
                              ))
    folder = forms.ChoiceField(label='folder', choices=(Folder.objects.values('id', 'name')),
                               )

    folder = forms.ModelChoiceField(queryset=Folder.objects.all(), empty_label="--- select destination ---",
                                    widget=forms.Select(attrs={'class': 'form-control input-sm'}))

    file = forms.FileField(label='Upload file',
                           widget=forms.FileInput(
                               attrs={'class': 'form-control input-sm', 'id': 'document-file',
                                      'accept': '.doc,.pdf,.docx'}))
