from django import forms

class folderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=50,
                                  widget= forms.TextInput(attrs={'placeholder':'Type Folder Name Here','class':'form-control input-sm'}) )
    status = forms.ChoiceField(label='Status', choices=(('','-- select folder attribute --'),(True, 'Hidden'),(False,'Unhide')),
                               widget= forms.Select(attrs={'class':'form-control input-sm'}),
                               )

class videoForm():
    pass

class pictureForm():
    pass

class documentForm():
    pass

class audioForm():
    pass


