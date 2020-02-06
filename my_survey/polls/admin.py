from django.contrib import admin
from polls.models import Question, Choice

# polls/admin.py
# Register your models here. => 관리자 페이지에서 데이터 관리 가능
admin.site.register(Question)
admin.site.register(Choice)