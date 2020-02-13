from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('join', views.JoinView.as_view(), name='join'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('<str:pk>/detail', views.MemberDetailView.as_view(), name='detail'),
]