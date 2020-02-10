from django.urls import path
from polls import views

app_name = 'polls'

# path(url, viewe함수)
urlpatterns = [
    path('list', views.list, name='list'),
    path('<int:question_id>/vote_form', views.vote_form, name='vote_form'),
    path('vote', views.vote, name='vote'),
    path('<int:question_id>/result', views.result, name='result')
]