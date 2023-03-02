from django import forms
from .models import Movie

class Movie_edit(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','Release','Description','Movie_Img']