from django.test import TestCase, Client
from .models import *

# Create your tests here.


class FileManagerTest(TestCase):

    def setUp(self):
        pass

    def testing_folder(self):
        c = Client()
        response = c.post('/folder',{'folder_name':'secret','status':True})
        self.assertEqual(response.status_code , 200)
