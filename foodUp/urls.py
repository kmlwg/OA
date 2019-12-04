from django.urls import path
from . import views
from .views import PostListView, ProfileDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', PostListView.as_view(), name='news'),
    path('search/', views.search, name='search'),
    path('newcompany/', views.newcompany, name='newcompany'),
    path('news/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('news/newpost/', PostCreateView.as_view(success_url='/news/'), name='new-post'),
    path('news/<int:pk>/update', PostUpdateView.as_view(success_url='/news/'), name='update-post'),
    path('news/<int:pk>/delete', PostDeleteView.as_view(success_url='/news/'), name='delete-post'),
]
