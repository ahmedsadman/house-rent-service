from accounts.models import UserProfile
from django import forms
from django.contrib.auth import get_user_model

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    phone_no = forms.CharField(required=True, max_length=11)
    address = forms.CharField(max_length=100)

    class Meta():
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
        )
