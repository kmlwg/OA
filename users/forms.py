from django import forms
#from django.contrib.auth.models import User
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    is_company = forms.NullBooleanField(initial=False)

    class Meta:
        model = User
        fields = ['username', 'is_company', 'password1', 'password2']
		

class EditProfile(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 'description', 'adres', 'email', 'time_opened', 'time_closed', 'phone_number', 'category']
		
