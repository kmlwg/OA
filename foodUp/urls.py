from django.urls import path, include
from django.views.generic import TemplateView

from .views import  index, UserProfileSignUpView, CompanyProfileSignUpView


urlpatterns = [
    path('', index, name='index'),
    path('register_user', UserProfileSignUpView.as_view(), name='register_user'),
    path('register_company', CompanyProfileSignUpView.as_view(), name='register_company'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
]