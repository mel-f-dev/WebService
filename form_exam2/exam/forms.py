from django import forms

from exam import models

# Form 클래스 작성: 요청 form의 입력 양식들을 관리하는 클래스.
# 입력받는 템플릿 작성, 전송된 요청파라미터를 읽고 검증하는 작업을 담당
# Form 클래스 - <form>, form 태그 하나당 하나씩
# 클래스 변수 - <input>, <select>, <textarea>: 한 개의 입력폼

class RegisterForm(forms.Form):
    # 클래스 변수: 변수명-name, 값-입력양식타입 객체
    # CharField - 문자열 입력받는 input 양식. - 기본 위젯:<input type=text>
    name = forms.CharField(max_length=100, label='사용자 이름', widget=forms.TextInput(attrs={'class':'form-control'})) # requered 디폴트 True
    age = forms.IntegerField(label='나이', widget=forms.NumberInput(attrs={'class':'form-control'}))
    
    # 원소(value, label)
    CHOICES = [
        ('Python', '파이썬'),
        ('Java', '자바'),
        ('Ruby', '루비')
    ]
    # ChoiceField - 여러개중에 한 개 선택
    # MultipleChoiceField - 여러개 중에 여러개 선택
    # 선택 항목을 리스트로 묶어서 전달.
    # 기본 위젯: select(radio-단일선택, checkbox-다중선택)

    # interest_language = forms.MultipleChoiceField(label='관심언어', 
    #                                             choices=CHOICES,
    #                                             widget=forms.CheckboxSelectMultiple)


    # modelChoiceField, ModelMultipleChocieField - 선택항목을 Model(데이터베이스)에서 가져온다.
    # value:PK 컬럼값, label:str()로 반환된 값.
    interest_language = forms.ModelMultipleChoiceField(label='취미',
                                                    widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check form-check-inline'}),
                                                    required=True,                                                                                            
                                                    queryset=models.Code.objects.filter(code_category='hobby'))

    # 사용자 정의 폼 검증 코드
    # 각 Field에 선언된 검증을 마친 다음에 호출된다.

    # 직접 정하는 검증 조건을 메소드로 만들어 준다.
    def clean(self):
        # 기본 검증을 통과한 요청 파라미터 조회             
        cleaned_data = super().clean()
        print(type(cleaned_data), cleaned_data)

        # 나이 > 0, 이름은 2글자 이상
        if cleaned_data.get('age') <= 0:
            # 에러 메세지 추가
            self.add_error("age", "나이는 1 이상을 넣으세요.")    # 입력태그의 name, 에러메세지
            
        if len(cleaned_data.get('name')) < 2:
            self.add_error('name', '이름은 2글자 이상 넣으세요.')