from django.test import TestCase, Client
from .models import *
from .forms import *

# Create your tests here.


class FileManagerTest(TestCase):

    def setUp(self):
        pass

    def testing_folder(self):
        c = Client()
        form = FolderForm(data = {'folder_name':'secret','status':True})

        response = c.post('/folder', form)
        self.assertEqual(response.status_code , 200)
