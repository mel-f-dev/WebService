from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView

from django.urls import reverse_lazy

from fileup.forms import PostRegisterForm
from fileup.models import Post
# fileup/views.py

# 게시물 등록 - 폼/처리  fileup/   templates/fileup
class PostRegisterView(FormView):
    template_name='fileup/register_form.html' #등록 폼 템플릿
    form_class = PostRegisterForm
    success_url = reverse_lazy('fileup:list') #등록 처리후 이동할 페이지

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        # 요청파라미터 조회 -> models.Post 저장 -> insert
        title = cleaned_data.get('title')
        info = cleaned_data.get('info')
        picture = cleaned_data.get('picture')
        file = cleaned_data.get('file')
        post = Post(title=title, info=info, picture=picture, file=file)
        post.save() #insert - 업로드된 파일이 지정된 디렉토리에 저장된다.
        return super().form_valid(form)

class PostList(ListView):
    model = Post
    template_name = 'fileup/list.html'   

class PostDetailView(DetailView):
    model = Post
    template_name = 'fileup/detail.html'