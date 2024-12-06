from django.urls import path
from api import views

urlpatterns = [
    path('', views.apod_view, name='apod'),
]
