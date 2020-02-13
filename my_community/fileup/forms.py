from django import forms

class PostRegisterForm(forms.Form):
    title = forms.CharField(
        max_length=200, 
        label='제목', 
        widget=forms.TextInput(attrs={'class':'form-control'}))

    info = forms.CharField(
        label='설명',
        widget=forms.Textarea(attrs={'class':'form-control'}))

    picture = forms.ImageField(
        label='사진',
        widget=forms.FileInput(attrs={'class':'form-control'})
    )

    file = forms.FileField(
        label='일반파일',
        widget=forms.FileInput(attrs={'class':'form-control'})   
    )