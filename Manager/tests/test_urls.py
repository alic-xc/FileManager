from django.test import SimpleTestCase
from django.urls import resolve, reverse
from Manager.views import *
#working on testing urls without connections to the server
class TestUrl(SimpleTestCase):

    def test_folder_resolved(self):
        url = reverse('folder')
        self.assertEqual(resolve(url).func, directory)

    def test_folder_list_resovled(self):
        url = reverse('view_folder', args=['ebd38308-59ff-40d1-b4f7-1b5c79d2f2a7'])
        self.assertEqual(resolve(url).func, view_directory )

    def test_audio_resolved(self):
        url = reverse('audio')
        self.assertEqual(resolve(url).func, audio)

    def test_audio_list_resolved(self):
        url = reverse('play_audio', args=['ebd38308-59ff-40d1-b4f7-1b5c79d2f2a7'])
        self.assertEqual(resolve(url).func, play_audio)

    def test_video_resolved(self):
        url = reverse('video')
        self.assertEqual(resolve(url).func, video)

    def test_video_list_resolved(self):
        url = reverse('play_video', args=['ebd38308-59ff-40d1-b4f7-1b5c79d2f2a7'])
        self.assertEqual(resolve(url).func, play_video)

    def test_document_resolved(self):
        url = reverse('document')
        self.assertEqual(resolve(url).func, document)

    def test_document_list_resolved(self):
        url = reverse('view_document', args=['ebd38308-59ff-40d1-b4f7-1b5c79d2f2a7'])
        self.assertEqual(resolve(url).func, view_document)
