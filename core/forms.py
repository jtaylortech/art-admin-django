from django import forms

from core.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["media_name", "imagefile"]