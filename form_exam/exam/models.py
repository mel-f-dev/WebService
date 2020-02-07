from django.db import models

# Create your models here.
# 사용자 - User
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.name, self.age)


# 관심언어
class InterestLanguage(models.Model):
    language = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.language    


# 코드 테이블
class Code(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    code_text = models.CharField(max_length=200)
    code_category = models.CharField(max_length=100)

    def __str__(self):
        return self.code_text


