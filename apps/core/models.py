from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class NgheNghiep(models.Model):
    code_job = models.IntegerField(default=0, null=True)
    name_job = models.CharField(max_length=255, default=None, null=True)
    job_info = RichTextUploadingField(default='')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Nghề nghiệp'
        verbose_name_plural = 'Nghề nghiệp'


class ThanhPho(models.Model):    
    name = models.CharField(max_length=255)
    code = models.IntegerField(default=0)
    group = models.IntegerField(default=0)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Tỉnh/thành phố '
        verbose_name_plural = 'Tỉnh/thành phố'