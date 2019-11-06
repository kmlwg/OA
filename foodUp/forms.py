from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
	user = forms.CharField(max_length=10, min_length=3)
	email = forms.EmailField()
	# company - depends on type of the account:
	# 0 - for User
	# 1 - for Company
	company = forms.BooleanField()

	class Meta:
		model = User
		fields = (
			'user',
			'email',
			'company',
			'password1',
			'password2'
		)
