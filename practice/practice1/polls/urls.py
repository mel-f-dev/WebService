from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('index', views.index, name='index'),
]