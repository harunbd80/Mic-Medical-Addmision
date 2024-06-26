from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class registrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    class Meta:
        fields=['username','password']