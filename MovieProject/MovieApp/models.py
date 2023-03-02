from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    Release = models.IntegerField()
    Description = models.TextField()
    Movie_Img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
