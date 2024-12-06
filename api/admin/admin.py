from django.contrib import admin
from api.models import Apod

class ApodAdmin(admin.modelAdmin):
  list_display = ('date', 'title', 'url' )

admin.site.register(Apod, ApodAdmin)