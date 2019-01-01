from datetime import datetime, timedelta
from django.db import models
from math import floor
from uuid import uuid4


class modifier(models.Manager):

    def created_recently(self):

        return super().get_queryset().filter(date__gte = datetime.now() - timedelta(days=1) ).order_by('date')


    def get_hidden_file(self):

        return super().get_queryset().filter(hidden=True)

    def get_unhide_entities(self):

        return super().get_queryset().filter(hidden=False)

    def get_all_files(self):

        



# Create your models here.
class Folder(models.Model):

    name = models.CharField('Folder Name', max_length=64, unique=True)
    unique = models.UUIDField('hash', default=uuid4, unique=True, editable=False)
    hidden = models.BooleanField(default=False)
    date = models.DateTimeField('date created',auto_now_add=True)

    # models managers
    objects = models.Manager()
    custom = modifier()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Folders'

    def get_all(self):



        pass

    def __str__(self):

        return f"{self.name}'s Folder "

class Videos(models.Model):

    formats = (("MP4","Mpeg 4"),("Avi","Audio Video Interface"),("MOV","Apple QuickTime Video"))

    name = models.CharField('Name',  max_length=64, unique=True, null=False)
    file_name = models.CharField('Unique',default=uuid4, max_length= 64, unique=True, null=False, editable=False)
    format = models.CharField('Format', choices=formats, max_length=3, null=False )
    size = models.IntegerField("Video Size", null=False)
    length = models.IntegerField('Video Length', null=False)
    width = models.IntegerField('Video Frame Width', null=False)
    height = models.IntegerField('Video Frame Height', null=False)
    summary = models.CharField('Video Summary', max_length=200, blank=False, null=False)
    hidden = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='movies')
    date = models.DateTimeField(auto_now_add=True)

    # models managers
    objects = models.Manager()
    custom = modifier()

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Videos'



    def lengthConverter(self, length:int ):

        hours = 0
        minutes = 0
        seconds = 0

        if length < 3600:

            minutes = floor(length / 60)
            seconds = length % 60

        if length >= 3600:

            hours = floor(length / 3600)
            minutes = floor((length % 3600) / 60)
            seconds = length % 60

        return f"{hours}:{minutes}:{seconds}"

    def __str__(self):

        return f" { self.name } - { self.size } ( {self.lengthConverter(self.length) }) ";





class Pictures(models.Model):
    formats = (("JPG", "joint Photographics Group"), ("GIF", "graphic interchange format"), ("PNG", "portable network graphic"))

    name = models.CharField('Name', max_length=64, unique=True, null=False)
    file_name = models.CharField('Unique',default=uuid4, max_length= 64, unique=True, null=False, editable=False)
    format = models.CharField('Format', choices=formats, max_length=3, null=False)
    size = models.IntegerField("Picture Size", null=False)
    width = models.IntegerField('picture Frame Width', null=False)
    height = models.IntegerField('picture Frame Height', null=False)
    summary = models.CharField('picture Summary', max_length=200, blank=False, null=False)
    hidden = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='gallery')
    date = models.DateTimeField(auto_now_add=True)

    # models managers
    objects = models.Manager()
    custom = modifier()

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Pictures'


    def __str__(self):

        return f"{self.name} - {self.size} ({ self.format })"



class Audio(models.Model):
    formats = (("MP3", "Mpeg 3"), ("WMA", "Windows Media Audio"), ("WAV", "Wave"))

    name = models.CharField('Name', max_length=64, unique=True, null=False)
    file_name = models.CharField('Unique',default=uuid4, max_length= 64, unique=True, null=False, editable=False)
    format = models.CharField('Format', choices=formats, max_length=3, null=False)
    size = models.IntegerField("Audio Size", null=False)
    length = models.IntegerField('Audio Length', null=False)
    summary = models.CharField('Audio Summary', max_length=200, blank=False, null=False)
    hidden = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='music')
    date = models.DateTimeField(auto_now_add=True)

    # models managers
    objects = models.Manager()
    custom = modifier()

    class Meta:

        ordering = ['date']
        verbose_name_plural = 'Audios'


    def lengthConverter(self, length:int ):

        hours = 0
        minutes = 0
        seconds = 0

        if length < 3600:

            minutes = floor(length / 60)
            seconds = length % 60

        if length >= 3600:

            hours = floor(length / 3600)
            minutes = floor((length % 3600) / 60)
            seconds = length % 60

        return f"{hours}:{minutes}:{seconds}"


    def __str__(self):

        return f"{self.name} - {self.size} ({ self.format })"


class Document(models.Model):
    formats = (("DOC", "Document"), ("PDF", "Portable Document Format"), ("MOV", "Apple QuickTime Video"))

    name = models.CharField('Name', max_length=64, unique=True, null=False)
    file_name = models.CharField('Unique',default=uuid4, max_length= 64, unique=True, null=False, editable=False)
    format = models.CharField('Format', choices=formats, max_length=3, null=False)
    size = models.IntegerField("Document Size", null=False)
    summary = models.CharField('Video Summary', max_length=200, blank=False, null=False)
    hidden = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='document')
    date = models.DateTimeField(auto_now_add=True)

    # models managers
    objects = models.Manager()
    custom = modifier()

    class Meta:

        ordering = ['date']
        verbose_name_plural = 'Documents'


    def __str__(self):

        return f"{self.name} - {self.size} ({ self.format })"