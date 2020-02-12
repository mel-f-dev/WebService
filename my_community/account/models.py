from django.db import models

# Create your models here.
# id/pw/이름/사진

class Member(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)    # 사용자가 지정한 값을 PK로
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='member_images')

    def __str__(self):
        return self.name