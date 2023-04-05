from django.db import models

# Create your models here.
class Moviedata(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    ratings = models.FloatField()
    type_movie = models.CharField(max_length=100,default='action')
    image = models.ImageField(upload_to='images/', default='noimage.jpg')
    
    def __str__(self):
        return self.name