from django import forms
from .models import User


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = User
        fields = ('first_name','image')