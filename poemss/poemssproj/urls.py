from django.contrib import admin
from django.urls import path
from poemssproj import views
urlpatterns = [
    path('', views.index, name='home'),
    path('article/', views.article, name='article'),
    path('poem/', views.poem, name='poem'),
    path('blog/', views.blog, name='blog'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('story/', views.story, name='story'),
    path('article/<int:post_id>', views.article, name= 'article'),
]
