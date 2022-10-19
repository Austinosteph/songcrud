from django.contrib import admin
from .models import artiste, song, lyric

admin.site.register(artiste)
admin.site.register(song)
admin.site.register(lyric)