from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class createuserform(UserCreationForm):
    class meta:
        model=User
        fields=['username','email','password','confirm_password']
