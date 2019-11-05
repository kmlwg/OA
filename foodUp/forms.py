from django import forms 
from .models import User, Company


class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'login',
			'password',
			'mail'
		]


class CompanyRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Company
		fields = [
			'login',
			'password',
			'mail'
		]
