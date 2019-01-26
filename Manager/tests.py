from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from .forms import *

import os
# Create your tests here.


class FileManagerTest(TestCase):

    def setUp(self):
        self.image1 = ''
        self.image2 = ''
        self.video1 = ''
        self.video2=''
        self.document1 = ''
        self.document2 = ''
        self.audio1 = ''
        self.audio2 = ''


    def testing_folder_form(self):
        form = FolderForm(data = {'folder_name':'secret','status':True})
        self.assertEqual(form.is_valid(), True)

    def testing_folder_view(self):
        # testing A
        response = self.client.post('/folder',{'folder_name':'secret_2','status':True})
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(os.path.exists('media/secret_2'))
        self.assertEqual(str(messages[0]), 'Folder created successfully')
        folder = Folder.objects.get(name='secret_2')
        self.assertEqual(folder.name, 'secret_2')

        # testing  B
        response = self.client.post('/folder',{'folder_name':'secret_2','status':True})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[1]), 'Name already exist')

    def testing_folder_node(self):
        response = self.client.post('/folder',{'folder_name':'music','status':True})
        uuid = Folder.objects.get(name='music')
        response1 = self.client.get(f'/folder/{uuid.unique}')
        self.assertEqual(response1.status_code, 200)

    # def testing_video(self):
    #     response = self.client.post('/video',)
    #     pass

    def tearDown(self):

        os.unlink('media/secret_2')
        os.unlink('media/music')
