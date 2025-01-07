from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blog(models.Model):
        title=models.CharField(max_length=200)
        sub_title=models.CharField( max_length=400,null=True)
        content=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)
        related_user=models.ForeignKey(User,related_name='blog_post',on_delete=models.CASCADE)