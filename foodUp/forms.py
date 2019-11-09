from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from foodUp.models import User, UserProfile, CompanyProfile 

class UserProfileSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=40, required=False)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        user_profile = UserProfile.objects.create(user=user)
        return user


class CompanyProfileSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=40, required=False)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company_profile = CompanyProfile.objects.create(user=user)
        return user



# class RegisterForm(UserCreationForm):
# 	user = forms.CharField(max_length=10, min_length=3)
# 	email = forms.EmailField()
# 	# company - depends on type of the account:
# 	# 0 - for User
# 	# 1 - for Company
# 	company = forms.BooleanField()

# 	class Meta:
# 		model = User
# 		fields = (
# 			'user',
# 			'email',
# 			'company',
# 			'password1',
# 			'password2'
# 		)