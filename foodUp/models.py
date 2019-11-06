from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	telephone = models.CharField(max_length=11, blank=True)
	email = models.EmailField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	"""

	:param sender:
	:param instance:
	:param created:
	:param kwargs:
	:return:
	"""
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
