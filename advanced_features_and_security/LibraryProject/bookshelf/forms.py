from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2')
