from django.db import models

class Apod(models.Model):
  title = models.TextField()
  date = models.TextField()
  explanation = models.TextField()
  rights = models.TextField()
  url = models.TextField()
  
  def __str__(self):
      return 'picture of the day ' + self.date