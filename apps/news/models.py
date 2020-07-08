from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True)
    link_video = models.CharField(max_length=255, null = True, default=None)
    sub_title = models.CharField(max_length=200)
    content = RichTextUploadingField(default='')
    images_gioi_thieu = models.TextField(null=True, default=None)
    sub_content = RichTextUploadingField(default='')
    seo_key_word = models.CharField(max_length=200, null = True, default=None)
    status = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Tin tức'
        verbose_name_plural = 'Tin tức'