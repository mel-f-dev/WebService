# fileup/urls.py
from django.urls import path
from fileup import views

app_name = 'fileup'

urlpatterns = [
    path('register', views.PostRegisterView.as_view(), name='register'),
    path('list', views.PostList.as_view(), name='list'),
    path('<int:pk>/detail', views.PostDetailView.as_view(), name='detail'),
]