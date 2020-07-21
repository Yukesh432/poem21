from django.urls import path
from . import views

urlpatterns= [
    path('login/', views.login, name= 'login'),
    path('join/', views.join, name= 'join'),
    path('logout/', views.logout, name= 'logout'),
    path('profile/', views.profile, name= 'profile'),
] 