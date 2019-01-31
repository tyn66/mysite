from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","content","author","is_delete","created_time","last_updated_time")#设置admin后台要现实的字段
    ordering = ("id",)#设置按照id正序排列，-id为倒序


#admin.site.register(Article,ArticleAdmin)