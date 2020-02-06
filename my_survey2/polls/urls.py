from django.urls import path    # path: 함수
from polls import views    # views.py를 import


# url 설정 이름의 prefix(namespace)로 사용.
# 필수사항은 아니다.
app_name = 'polls'    # 접두어를 줌으로써 url검색이 쉬워짐 polls:index(->path name)


# path 함수가 리턴시키는 값이 리스트 안으로
# urls.py에서 polls/ 까지 인식, 그 이하 값을 인지하면 된다.
urlpatterns = [
    # path(url, view)
    # 이름으로 특정한 설정값을 호출하기 쉬워짐
    path('index', views.index, name='index'), # polls 밑에 index라는 url로 들어오면 views파일 index함수가 일을 할 것!, 설정 이름은 index
    path('list', views.list, name='list'),
    # 투표 form 제공. polls/1/vote_form
    path('<int:question_id>/vote_form', views.vote_form, name='vote_form'),    # int: 컨버터, 들어올 값의 자료형태
    path('vote', views.vote, name='vote'),
    path('<int:question_id>/result', views.result, name='result'),    # 투표결과
    # polls/3/result: 3번 질문 결과
]



