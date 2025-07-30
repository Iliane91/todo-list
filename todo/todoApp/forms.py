from django import forms
from todoApp.models import Task
from django.contrib.auth.forms import AuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user']



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Nom d'utilisateur"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
    )