from django.shortcuts import render, redirect
from datetime import datetime
from polls.models import Question, Choice
from django.http import HttpResponse
from django.urls import reverse    # url이름으로 경로 조회하는 메소드

# Create your views here.

# polls/index 요청을 처리하는 view 함수
# 첫번째 매개변수: request - HTTP 요청 관련 기능 or 정보 제공.
# view의 역할 : 사용자 요청을 처리
# view에 작성할 것 : 사용자 요청작업 처리 + Template호출(처리결과 응답) 호출

def index(request):
    currentTime = datetime.now()
    return render(request, "polls/index.html", {'current':currentTime})    # render: 처리결과 호출


def list(request):
    # 함수 task : 질문들을 조회
    question_list = Question.objects.all() 
    # 응답페이지 (template: polls/list.html)로 이동.
    # render(): 어느 template으로 이동할지 설정. HttpResponse반환.
    return render(request, "polls/list.html", {'q_l':question_list, 'message':'2회'})


# vote_form(설문 page)을 응답하는 view.
# (request, url에서 전송된 값을 받을 변수[들])
def vote_form(request, question_id):    # question_id : urls.py의 <int:question_id>에서 사용한 변수명 
    # 질문 조회
    try:
        question = Question.objects.get(pk=question_id)
        return render(request, 'polls/detail.html', {'question':question})    
    except Exception as e:
        return list(request)    

# 투표
# 요청파라미터 조회 : request.POST -> QueryDic 
#                                   -> ['요청 파라미터 이름'] or get('이름') or
#                                   getlist('이름'): 같은 이름으로 여러개가 넘어온 경우
def vote(request):
    # 요청 파라미터 조회
    question_id = request.POST.get('question_id')
    choice_id = request.POST.get('choice')

    # 요청 파라미터 검증    
    if not choice_id: # choice로 넘어온 값이 없으면 -> 투표 form으로 이동
        question = Question.objects.get(pk=question_id)
        return render(request, 
                    'polls/detail.html',
                    {'question':question, 'error_message':"보기를 선택하세요."})

    # 요청 처리 - Business Logic
    # Choice select
    selected_choice = Choice.objects.get(pk=choice_id)
    selected_choice.votes += 1    # votes 값을 1 증가
    selected_choice.save()    # 변경 내용 update

    # 응답: views.result <- 리다이렉트 방식으로 응답
    # <int:question_id>/result -> ex) /polls/2/result
    # return redirect('http://www.naver.com')
    # return render(request, 'polls/index.html')    # 데이터 변경이 있을 때는 render가 아닌 redirect 방식으로 웹브라우저를 요청하도록
    return_url = reverse("polls:result", args=[question_id])
    print(return_url)
    return redirect(return_url)


# 투표결과 - polls/3/result
def result(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/result.html', {'question':question})