from django.urls import path
from polls import views

# path(url, 처리할 함수, name = '설정명') -> url과 views에서 만든 함수를 연결해주는 코드
urlpatterns = [
    
    path('', views.index2, name='index2'),
    path('index', views.index, name='index'), 

]