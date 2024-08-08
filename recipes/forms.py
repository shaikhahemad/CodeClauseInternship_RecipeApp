from django import forms
from .models import RecipeModel

class RecipeForm(forms.ModelForm):
  class Meta:
    model = RecipeModel
    fields = ['name', 'description', 'ingredients', 'duration', 'image']
    widgets = {
      
    'name': forms.TextInput(attrs={'class': ''}),
    'description': forms.TextInput(attrs={'class': ''}),
    'ingredients': forms.TextInput(attrs={'class': ''}),
    'duration': forms.NumberInput(attrs={'class': ''}),
    'image': forms.ClearableFileInput(attrs={'class': ''}),
    }