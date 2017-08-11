from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserSignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )


class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'location')
