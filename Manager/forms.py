from django import forms

class folderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=50)
    hidden = forms.BooleanField(label='Hidden')

class videoForm():
    pass

class pictureForm():
    pass

class documentForm():
    pass

class audioForm():
    pass


