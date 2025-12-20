from django import forms
from products.models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product name'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Description'}),
            'mark': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Mark'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
        }