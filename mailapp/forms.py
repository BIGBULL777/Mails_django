from django.forms import forms
from .models import *
from .models import *
from django import forms
from django.forms import ModelForm,widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SendMailForm(forms.ModelForm):
    class Meta():
        model = SendMail
        fields = '__all__'
