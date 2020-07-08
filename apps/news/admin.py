from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug','sub_title','content','images_gioi_thieu','sub_content','seo_key_word','status','created_time')


admin.site.register(Article, ArticleAdmin)
