from django.contrib.auth.models import User
from django.forms import forms


class RegistrationForm(forms.Form):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'username')


class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'username')


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'password')
