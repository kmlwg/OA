from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver

# Create your models here.

# Wspólna tabela dla użytkownika firmowego i normalnego,
# rozróznienie w całej aplikacji następuje przez flagę is_comapny
class User(AbstractUser):
    is_company = models.BooleanField(default=False)


# TODO Powiąznie UserProfile z CompanyProfile, żeby użykownik mógł ocnieniać restauracje tylko raz
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False, related_name='user_profile')
    phone_number = models.CharField(max_length=11)


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False, related_name='company_profile')
    name = models.CharField(max_length=40, unique=True)
    phone_number = models.CharField(max_length=11)
    time_opened = models.TimeField()
    time_closed = models.TimeField()
    rating = models.FloatField(validators=[MaxValueValidator(10.0), MinValueValidator(0.0)], default=0.0)
    description = models.TextField()


class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    building_number = models.IntegerField(validators=[MinValueValidator(1)])
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=20)
    companies = models.ManyToManyField(CompanyProfile)

    class Meta:
        ordering = ['name']


# @receiver(models.signals.post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	print('****', created)
# 	if instance.user_type == 1:
# 	    UserProfile.objects.get_or_create(user = instance)
# 	else:
# 		CompanyProfile.objects.get_or_create(user = instance)
	
# @receiver(models.signals.post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	print('_-----')	
# 	if instance.user_type == 1:
# 		instance.user_profile.save()
# 	else:
# 		CompanyProfile.objects.get_or_create(user = instance)







