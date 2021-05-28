from django.db import models

# Create your models here.

class Post(models.Model):
  image = models.ImageField(upload_to='posts/images/')
  title = models.CharField(max_length=200)
  
  def __str__(self):
    return self.title
