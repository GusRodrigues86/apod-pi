from django.shortcuts import render
from api.models import Apod

def apod_view(request):
  return render(request, 'main/apod.html', {})