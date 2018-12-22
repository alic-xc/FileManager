from django import forms

class folderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=50,
                                  widget= forms.TextInput(attrs={'placeholder':'Type Folder Name Here','class':'form-control'}) )
    status = forms.ChoiceField(label='Status', choices=((True, 'Hidden'),(False,'Unhide')))

class videoForm():
    pass

class pictureForm():
    pass

class documentForm():
    pass

class audioForm():
    pass


