from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from foodUp.models import User, UserProfile 

class UserProfileSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=11, required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    # @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.save()
        user_profile = UserProfile.objects.create(user=user)
        user_profile.phone_number = self.phone_number
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