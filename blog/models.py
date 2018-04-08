from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='경도,위도 포맷으로 입력', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)