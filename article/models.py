from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)#设置时间自动生成
    last_updated_time = models.DateTimeField(auto_now=True)#自动修改成现在时间
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)
    is_delete = models.BooleanField(default=False)
    readed_num = models.IntegerField(default=0)


    def __str__(self):
        return '<Article:%s>' % self.title#在后台可以看到标题