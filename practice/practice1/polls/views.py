from django.shortcuts import render
from datetime import datetime

def index(request):
    currentTime = datetime.now()
    return render(request, 'polls/index.html', {'current':currentTime})
