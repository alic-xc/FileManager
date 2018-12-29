from django.urls import path
from .views import *


urlpatterns = [
    path('',homepage, name='home'),

    path('folder', directory, name='folder'),
    path('folder/<uuid:folder>', view_directory, name='view_folder'),

    path('video', video, name='video'),
    path('video/<uuid:filename>/access', play_video, name = 'play_video'),

    path('audio', audio, name='audio'),
    path('audio/<uuid:filename>/access', play_audio, name = 'play_audio'),

    path('picture', picture, name='picture'),
    path('picture/<uuid:filename>', view_picture, name='view_picture'),

    path('document', document, name="document"),
    path('document/<uuid:filename>', view_document, name='view_document')


]

