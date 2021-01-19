

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate,login

class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=30,required=True,label='Email Address')

    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.get(email=email)
            result = authenticate(username=user.username,password=password)
            if result is not None:
                #save this data in session
                login(self.request,result)
                return result
            raise ValidationError('Email or password invalid')
        except:
            raise ValidationError('Email or password invalid')




