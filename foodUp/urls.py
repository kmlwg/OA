from django.urls import path

from .views import  index
# UserProfileSignUpView
urlpatterns = [
    path('', index, name='index'),
    path('register', UserProfileSignUpView.as_view(), name='register')
]