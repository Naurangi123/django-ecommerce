from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update'),
]
