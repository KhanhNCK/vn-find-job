from django.contrib import admin
from .models import NgheNghiep, ThanhPho
# Register your models here.

class NgheNghiepAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_job', 'code_job','job_info')


class ThanhPhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code','group','longitude','latitude')


admin.site.register(NgheNghiep, NgheNghiepAdmin)
admin.site.register(ThanhPho, ThanhPhoAdmin)