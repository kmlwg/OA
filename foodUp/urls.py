from django.urls import path

from .views import  index, UserProfileSignUpView, CompanyProfileSignUpView


urlpatterns = [
    path('', index, name='index'),
    path('register_user', UserProfileSignUpView.as_view(), name='register_user'),
    path('register_company', CompanyProfileSignUpView.as_view(), name='register_company'),
]