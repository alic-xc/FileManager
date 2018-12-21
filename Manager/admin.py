from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Audio)
admin.site.register(Document)
admin.site.register(Folder)
admin.site.register(Pictures)
admin.site.register(Videos)

