from django.urls import path
from exam import views

app_name = 'exam'

urlpatterns = [
    path('register', views.RegisterView.as_view(), name = 'register'),
    path('list', views.UserList.as_view(), name='userlist'),
    path('<int:pk>/detail', views.UserDetail.as_view(), name='userdetail'),
]