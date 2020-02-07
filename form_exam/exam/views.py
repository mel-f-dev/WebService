from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, DetailView

from exam.models import User, InterestLanguage, Code
# Create your views here.
# 등록 폼 + 등록 처리 View
class JoinView(View):
    def get(self, request, *args, **kwargs):
        lang = Code.objects.filter(code_category = 'language')
        return render(request, 'exam/join_form.html', {'lang':lang}) 

    def post(self, request, *args, **kwargs):
        # 1. 요청 파라미터 조회
        name = request.POST.get('name')    # 문자열
        age = request.POST.get('age')    # 문자열
        interest_language_list = request.POST.getlist('interest_language')   # 리스트, 같은 이름으로 여러개 넘어올 때
        print(name, age, interest_language_list)
        # 2. 요청 파라미터 검증
        if not (name and age and interest_language_list):
            lang = Code.objects.filter(code_category = 'language')
            return render(request, 'exam/join_form.html', {"error_message":"이름, 나이, 관심언어를 입력하세요.", "lang":lang})

        # 3. 처리 - 저장
            # User insert
        user = User(name=name, age=age)
        user.save()    # insert. insert 후에 pk를 user 객체에 할당

        for interest in interest_language_list:
            i_lang = InterestLanguage(language = interest, user= user)    # models.py 참고
            i_lang.save()
        
            # 4. 응답 - render() / redirect()-변경(insert, update, delete)
        return redirect(reverse('exam:detail', args=[user.pk]))   # name을 가진 url 가져오기


# 한 User 정보 조회 view
class UserDetailView(DetailView):
    model = User
    template_name = 'exam/user_detail.html'

    # {object:조회한 user} {user:User}
