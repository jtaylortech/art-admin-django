from django.contrib import admin
from core.models import Location, Artwork, Description, ArtDiscovery, Image

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    pass

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(ArtDiscovery)
class ArtDiscoverAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass