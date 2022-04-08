from django import forms
from .models import Pupil


class PupilForm(forms.ModelForm):
    class Meta:
        model = Pupil
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'})
        }