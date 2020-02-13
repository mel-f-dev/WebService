from django.db import models

# Create your models here.
# (글+이미지+파일)로 구성된 게시물
class Post(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()    # 대용량 텍스트

    # upload 된 이미지 정보. DB저장시 image로 경로가 저장된다.
    # upload_to: MEDIA_ROOT/images
    picture = models.ImageField(upload_to='images')
    file = models.FileField()