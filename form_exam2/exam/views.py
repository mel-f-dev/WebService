from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.urls import reverse_lazy

from exam.forms import RegisterForm
from exam import models

# Create your views here.
# 등록처리 View - 등록양식응답, 등록처리 => Form Class 이용:FormView 상속 받기
class RegisterView(FormView):
    template_name = 'exam/register_form.html'    # 입력양식 템플릿 지정. 입력폼 위치를 알려줌.
    form_class = RegisterForm
    success_url = reverse_lazy('exam:userlist')   # 등록 처리 후 이동할 url(리다이렉트 방식 이용). 등록 성공했을 때 이동할 위치.

    # 요청파라미터를 처리하는 비즈니스 로직 작성.
    # 호출시점: 요청파라미터 검증 끝나고 에러메세지가 없을 때 호출.
    def form_valid(self, form):    # form: 검증 끝난 요청파라미터.
        name = form.data.get('name')
        age = form.data.get('age')
        interest_language = form.data.getlist('interest_language')
        user = models.User(name=name, age=age)
        user.save()

        for lang in interest_language:
            language = models.InterestLanguage(language=lang, user=user)
            language.save()

        return super().form_valid(form)

class UserList(ListView):
    template_name = 'exam/user_list.html'    
    model = models.User
    paginate_by = 5    # 한 페이지에 보여질 데이터 수

    # template에 전달할 context 변수 생성
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        page_numbers_range = 5    # 페이지 그룹의 페이지 개수
        paginator = context.get('paginator')
        max_page = paginator.num_pages    # 총 페이지 수

        page_tmp = self.request.GET.get('page')    # self.request : 요청정보인 HttpRequest 객체 반환
        current_page = int(page_tmp if page_tmp else 1)
        # url?page=3    exam/list

        start_index = int((current_page-1)/page_numbers_range)*page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index > max_page:
            end_index = max_page
        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        print(context)

    


        return context




class UserDetail(DetailView):
    template_name = 'exam/user_detail.html'
    model = models.User

