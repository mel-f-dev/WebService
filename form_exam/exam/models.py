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