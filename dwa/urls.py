"""AA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('foodUp.urls')),
	path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
	path('login/', auth_views.LoginView.as_view(template_name=
	'users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name=
	'users/logout.html'), name='logout'),
	path('editprofile/', user_views.editprofile, name='editprofile'),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)