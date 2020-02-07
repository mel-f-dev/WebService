"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from config import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    # 사용자가 polls라는 경로로 시작해서 접속하면 polls.urls의 설정들을 확인하라는 명령
    # 파일을 등록할 땐 include 사용
    path('polls/', include('polls.urls')),    # polls 패키지에 있는 urls로 이동하도록 설정
    
]
