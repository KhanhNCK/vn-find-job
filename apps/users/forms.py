from django import forms
# from captcha.fields import ReCaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'input100', 'placeholder':'Địa chỉ email', 'type':'email', 'name':'username'}))
    password = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'type': 'password', 'class': 'input100', 'placeholder':'Mật khẩu', 'name':'password'}))


# class FormWithCaptcha(forms.Form):
#     captcha = ReCaptchaField()

#     class Meta:
#         fields = ('captcha')