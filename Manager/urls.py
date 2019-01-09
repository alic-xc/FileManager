from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',homepage, name='home'),

    path('folder', directory, name='folder'),
    path('folder/<uuid:folder>', view_directory, name='view_folder'),

    path('video', video, name='video'),
    path('video/<uuid:filename>/play', play_video, name = 'play_video'),

    path('audio', audio, name='audio'),
    path('audio/<uuid:filename>/play', play_audio, name = 'play_audio'),

    path('picture', picture, name='picture'),
    path('picture/<uuid:filename>/preview', view_picture, name='view_picture'),

    path('document', document, name="document"),
    path('document/<uuid:filename>/preview', view_document, name='view_document')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

