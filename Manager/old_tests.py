from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
from .forms import *

import os
# Create your tests here.


class FileManagerTest(TestCase):

    def setUp(self):
        self.image1 = 'testing/image.jpg'
        self.image2 = 'testing/image2.jpg'
        self.video1 = 'testing/video.mp4'
        self.video2='testing/video2.mp4'
        self.document1 = 'testing/doc.docx'
        self.document2 = 'testing/doc2.docx'
        self.audio1 = 'testing/audio.mp3'
        self.audio2 = 'testing/audio2.mp3'


    # def testing_folder_form(self):
    #     form = FolderForm(data = {'folder_name':'secret','status':True})
    #     self.assertEqual(form.is_valid(), True)
    #
    # def testing_folder_view(self):
    #     # testing A
    #     response = self.client.post('/folder',{'folder_name':'secret_2','status':True})
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertTrue(os.path.exists('media/secret_2'))
    #     self.assertEqual(str(messages[0]), 'Folder created successfully')
    #     folder = Folder.objects.get(name='secret_2')
    #     self.assertEqual(folder.name, 'secret_2')
    #
    #     # testing  B
    #     response = self.client.post('/folder',{'folder_name':'secret_2','status':True})
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(str(messages[1]), 'Name already exist')
    #
    # def testing_folder_node(self):
    #     response = self.client.post('/folder',{'folder_name':'music','status':True})
    #     uuid = Folder.objects.get(name='music')
    #     response1 = self.client.get(f'/folder/{uuid.unique}')
    #     self.assertEqual(response1.status_code, 200)

    def testing_video(self):
        response = self.client.post('/folder',{'folder_name':'secret_2','status':True})
        with open(f'media/{self.video1}', mode='rb') as file:
            response1 = self.client.post('/video',{'name':'testing',
         'summary':'my best music','size':25000,'folder':1,'file':file})
        print(Videos.objects.all())

        # messages = list(get_messages(response.wsgi_request))
        # print(str(messages[0]))
        # self.assertIsNotNone(Videos.objects.all())
        print(response1.)
        self.assertEqual(response1.status_code, 200)


    def testing_video_list(self):

        pass

    # def tearDown(self):
    #     if os.path.exists('media/secret_2'):
    #         os.rmdir('media/secret_2')
    #     if os.path.exists('media/music'):
    #         os.rmdir('media/music')
