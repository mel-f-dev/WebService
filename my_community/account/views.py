from django.shortcuts import render
from django.views.generic import FormView

# 패스워드 암호화 해주는 함수.
from django.contrib.auth.hashers import make_password

from account.forms import MemberJoinForm, LoginForm
from account.models import Member
# Create your views here.

# 가입처리
class JoinView(FormView):
    template_name = 'account/join_form.html'
    form_class = MemberJoinForm
    success_url = '/'    # 메인으로

    # 검증이 끝난 Form을 받아서 비즈니스 로직(가입처리) 처리하는 함수.
    def form_valid(self, form):
        cleaned_data = form.cleaned_data    # dictionary
        email = cleaned_data.get('email')
        password = make_password(cleaned_data.get('password'))   # 암호화 처리
        name = cleaned_data.get('name')
        picture = cleaned_data.get('picture')
        member = Member(email=email, password=password, name=name, picture=picture)
        member.save()

        return super().form_valid(form)
    

# 로그인 처리 View
class LoginView(FormView):
    template_name = 'account/login_form.html'
    form_class = LoginForm
    success_url = '/'    # 메인으로

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        email = cleaned_data.get('email')    # db에 저장되어 있는 email
        # Session객체-dictionary 형태:key-value쌍이 필요
        # 로그인 -> session에 로그인 여부를 확인할 수 있는 체크값을 넣어둔다.
        self.request.session['user'] = email    # request: HttpRequest(사용자 HTTP 요청정보)

        return super().form_valid(form)


# 로그아웃
def logout(request):
    request.session.clear()    # 세션에 저장된 세션데이터를 모두 제거.

    return render(request, 'home.html')

