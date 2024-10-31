from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('blog/<int:publicationId>/', views.blog, name='blog'),
]