from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


class User(AbstractUser):
	is_company = models.BooleanField(default = False)
	
	def __str__(self):
		return self.username
		
class Profile(models.Model):
	FOOD_CHOICES = (
		('pizza', 'pizza'),
		('beer', 'beer'),
		('pasta', 'pasta'),
		('burger', 'burger'), 
	 )
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.TextField()
	logo = models.ImageField(default='default.jpg', upload_to='profile_pics')
	description = models.TextField(default='')
	email = models.EmailField(default='')
	adres = models.TextField()
	phone_number = models.TextField(default='')
	time_opened = models.TimeField(null=True)
	time_closed = models.TimeField(null=True)
	rate = models.DecimalField(default=0.0, max_digits = 5, decimal_places=2)
	category = MultiSelectField(choices = FOOD_CHOICES, default=None)
	
	def __str__(self):
		return self.user.username
		

class Favourites(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

