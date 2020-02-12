from django import forms
from account.models import Member


# 회원가입 폼
class MemberJoinForm(forms.Form):
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'class':'form-control'})

    )
    re_password = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(attrs={'class':'form-control'}))
    picture = forms.ImageField(
        label='사진',
        widget=forms.FileInput(attrs={'class':'form-control'})
    )