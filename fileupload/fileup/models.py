from django.db import models

# fileup/models.py
# 글 + 이미지 + 파일 로 구성된 게시물.
class Post(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField() # 대용량 텍스트

    # upload된 이미지 정보. DB 저장시 images 경로가 저장된다.
    # upload_to : MEDIA_ROOT/images
    picture = models.ImageField(upload_to='images')
    file = models.FileField()
