from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "نام کاربری خود را تایپ کنید",
                                                             'class': 'input100',
                                                             }))

    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل',
                                                           'class': 'input100',
                                                           }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را وارد کنید',
                                                                  'class': 'input100',
                                                                  }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را مجددا وارد کنید',
                                                                  'class': 'input100',
                                                                  }))