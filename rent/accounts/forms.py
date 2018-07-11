from accounts.models import UserProfile
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    phone_no = forms.CharField(required=True, max_length=13, widget=forms.TextInput(attrs={'placeholder': 'Phone No'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta():
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )


# this is created only to add the extra placeholders :(
class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'validate', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(
        attrs={'placeholder': 'Password'}))
