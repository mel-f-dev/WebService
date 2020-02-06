from django.db import models

# Create your models here.

# 설문 질문
class Question(models.Model):
    # 컬럼변수 = 타입 관련 객체
    question_text = models.CharField(max_length=200)   # 200글자 까지 저장
    pub_date = models.DateTimeField()


# 특수매소드
    def __str__(self):  
        return self.question_text



class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # on_delete=cascade : 종속된 것 함께 삭제

    def __str__(self):
        return self.choice_text