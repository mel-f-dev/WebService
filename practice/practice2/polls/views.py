from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from polls.models import Question, Choice



# Create your views here.

def list(request):
    question_list = Question.objects.all()
    return render(request, "polls/list.html", {'q_l':question_list})


def vote_form(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        return render(request, 'polls/vote_form.html', {'selected_question':question})
    except Exception as e:
        return list(request)


def vote(request):
    # 요청 파라미터 조회
    question_id = request.POST.get('question_id')
    choice_id = request.POST.get('choice')

    # 요청 파라미터 검증
    if not choice_id:
        question = Question.objects.get(pk=question_id)
        return render(request, 
                    'polls/vote_form.html', 
                    {'selected_question':question, 'error_messsage':"보기를 선택하세요."})

    # 요청 처리 - Business Logic
    selected_choice = Choice.objects.get(pk=choice_id)
    selected_choice.votes += 1
    selected_choice.save()

    return_url = reverse("polls:result", args=[question_id])
    print(return_url)
    return redirect(return_url)



def result(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/result.html', {'selected_question':question})