from django.shortcuts import render
from django.views.generic import FormView

# 패스워드 암호화 해주는 함수.
from django.contrib.auth.hashers import make_password

from account.forms import MemberJoinForm
from account.models import Member
# Create your views here.

# 가입처리
class JoinView(FormView):
    template_name = 'account/join_form.html'
    form_class = MemberJoinForm
    success_url = '/'
    