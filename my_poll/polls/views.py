from django.shortcuts import render

from django.http import HttpResponse
import datetime

# Create your views here.
# ﻿http://ip:8000/polls/index 요청을 처리하는 함수.

def index(request):
    current = datetime.datetime.now()
    return HttpResponse("<h1>안녕하세요. :D</h1>"+str(current))


# http://127.0.0.1:8000/polls/ 요청처리.
def index2(request):
    current = datetime.datetime.now()
    # polls/index.html이 응답이 되도록 호출
    # render(request, 'html경로', html에 전달할 값들(dictionary))
    # html : template파일
    # html에 전달할 값 - context 파라미터
    return render(request, 'polls/index.html', {'current':current})