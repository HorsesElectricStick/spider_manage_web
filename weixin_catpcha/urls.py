from django.urls import path
from . import views

app_name = 'weixin_catpcha'

urlpatterns = [
    path(r'captcha/', views.获取验证码, name='获取验证码'),
]