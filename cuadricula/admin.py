from django.contrib import admin

from .models import Album, Artist, Genre

from django.contrib import admin


admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
