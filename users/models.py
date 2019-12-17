from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from multiselectfield import MultiSelectField
from star_ratings.models import Rating



class User(AbstractUser):
    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    FOOD_CHOICES = (
        ('pizza', 'pizza'),
        ('beer', 'beer'),
        ('pasta', 'pasta'),
        ('burger', 'burger'),
        ('cake', 'cake'),
        ('chinese', 'chinese'),
        ('soup', 'soup'),
        ('pancakes', 'pancakes'),
        ('dumplings', 'dumplings'),
    )
    PRICE_CHOICES = (
        ('$', '$'),
        ('$$', '$$'),
        ('$$$', '$$$'),
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
    ratings = GenericRelation(Rating, related_query_name='profiles')
    category = MultiSelectField(choices=FOOD_CHOICES, default=None)
    price = MultiSelectField(choices=PRICE_CHOICES, default=None)

    def __str__(self):
        return self.user.username


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)