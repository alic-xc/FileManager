from django import forms

class folderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=50,
                                  widget= forms.TextInput(
                                      attrs={'placeholder':'Type Folder Name Here','class':'form-control input-sm'}) )
    status = forms.ChoiceField(label='Status',
                               choices=(('','-- select folder attribute --'),(True, 'Hidden'),(False,'Unhide')),
                               widget= forms.Select(attrs={'class':'form-control input-sm'}),
                               )

class videoForm():
    pass

class pictureForm():
    pass

class documentForm():
    pass

class audioForm(forms.Form):

    name = forms.CharField(label='Audio Name', max_length=50,
                                 widget=forms.TextInput(
                                     attrs={'placeholder':'Enter Name Here','class':'form-control input-sm'}))
    format = forms.ChoiceField(label='Audio Format',
                             choices=(('','--select Audio format--'),('MP3','MP3'),('WMA','WMA'),('WAV'),('WAV')),
                             widget=forms.TextInput(
                                 attrs={'class':'form-control input-sm'}
                             ))
    summary = forms.CharField(label='Audio Summary', max_length=200,
                              widget=forms.TextInput(
                                  attrs={'placeholder':'Enter Audio Summary','class':'form-control input-sm'}
                              ))


