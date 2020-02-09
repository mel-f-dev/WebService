from django.shortcuts import render, redirect
from polls.models import Question, Choice
from django.urls import reverse

# Create your views here.

def list(request):
    question_list = Question.objects.all()
    return render(request, 'polls/list.html', {"q_list":question_list})

def vote_form(request, question_id):
    try:
        selected_q = Question.objects.get(pk=question_id)
        return render(request, 'polls/vote_form.html', {'selected_q':selected_q})
    except Exception as e:
        return list(request)

def vote(request):
    question_id =  request.POST.get('question_id')
    choice_id = request.POST.get('choice')

    if not choice_id:
        selected_q = Question.objects.get(pk=question_id)
        return render(request, 
                    'polls/vote_form.html', 
                    {'selected_q':selected_q, 'error_message':'보기를 선택하세요.'})
    
    selected_c = Choice.objects.get(pk=choice_id)
    selected_c.votes += 1
    selected_c.save()

    return_url = reverse("polls:result", args=[question_id])    # reverse: url이름으로 경로조회
    print(return_url)
    return redirect(return_url)



def result(request, question_id):
    selected_q = Question.objects.get(pk=question_id)
    return render(request, 'polls/result.html', {'selected_q':selected_q})
