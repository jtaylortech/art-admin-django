from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Location(models.Model):
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    country = models.TextField()

class Artwork(models.model):
    art_piece = models.TextField()
    year_created = models.TextField()

class Description(models.model):
    subject = models.TextField()
    Text = models.TextField()

class ArtDiscovery(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)

class Image(models.Model):
    media_name = models.CharField(max_length=500) 
    media_file = models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile) 