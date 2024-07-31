from django import forms
from .models import gallery

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = gallery
        fields = ('title', 'image', 'status')