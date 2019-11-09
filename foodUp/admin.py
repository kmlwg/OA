from django.contrib import admin
from foodUp.models import User, UserProfile, CompanyProfile, Tag, Address

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(CompanyProfile)
admin.site.register(Tag)
admin.site.register(Address)
