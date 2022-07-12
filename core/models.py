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











































