from django.urls import path

from exam import views

app_name = 'exam'

urlpatterns = [
    path('join', views.JoinView.as_view(), name='join'),
    path('<int:pk>/detail', views.UserDetailView.as_view(), name='detail'),

    # /exam/2/detail
]