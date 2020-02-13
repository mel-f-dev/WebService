from django.shortcuts import redirect
from django.urls import reverse


# 로그인 여부를 체크하는 decorator 함수
# 로그인 안한 경우 login form으로 이동

# decorator 구현: 함수를 받아서 그 함수를 사용하는 함수를 정의한 뒤 반환
def login_required(function):

    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if not user: # 로그인 하지 않았다면
            return redirect(reverse('account:login'))

        return function(request, *args, **kwargs)

    return wrap