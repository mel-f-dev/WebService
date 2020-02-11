from django.db import models

# Create your models here.

# Code테이블 연동 모델
class Code(models.Model):
    code = models.CharField(max_length=100, primary_key=True)    # 기본적으로 primary key 값을 name으로
    code_text = models.CharField(max_length=100)                 # str이 반환해주는 값을 label
    code_category = models.CharField(max_length=200)

    def __str__(self):
        return self.code_text

# User 테이블 연동 모델
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class InterestLanguage(models.Model):
    language = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.language
