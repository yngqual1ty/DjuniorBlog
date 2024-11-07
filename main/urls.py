from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('createBlog/', views.createBlog, name='createBlog'),
    path('blog/<int:publicationId>/', views.blog, name='blog'),
    path('deleteBlog/<int:publicationId>/', views.deleteBlog, name='deleteBlog'),
    path('editBlog/<int:publicationId>/', views.editBlog, name='editBlog'),

    path('accounts/logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]