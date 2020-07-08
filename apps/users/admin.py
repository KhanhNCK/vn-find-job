from django.contrib import admin

from .models import Token, LoginHistory, User

class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')


class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'start_date', 'end_date', 'num_date')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'fullname', 'gender', 'birth_day', 'dia_chi_tinh_thanh_pho', 'dia_chi_quan_huyen', 'dia_chi_chi_tiet', 'loai_user')



admin.site.register(Token, TokenAdmin)
admin.site.register(LoginHistory, LoginHistoryAdmin)
admin.site.register(User, UserAdmin)
