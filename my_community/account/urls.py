from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('join', views.JoinView.as_view(), name='join'),
]