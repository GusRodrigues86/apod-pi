from django.contrib import admin
from api.models.apod_model import Apod

class ApodAdmin(admin.ModelAdmin):
  list_display = ('date', 'title', 'url' )
  list_filter = ('title', )
  search_fields = ('date',)

admin.site.register(Apod, ApodAdmin)