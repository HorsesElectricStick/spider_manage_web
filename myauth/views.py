from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from weixin_catpcha.models import *
from datetime import datetime

# Create your views here.

def 登录(request, info=None):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['用户名'], password=request.POST['密码'])
        if user is None:
            return render(request, 'myauth/login.html', {'错误': '用户名/密码错误!', 'username': request.POST['用户名']})
        else:
            验证码 = captcha.objects.filter(username_id=user.id)[0].captcha
            if 验证码 is None:
                return render(request, 'myauth/login.html', {'错误': '请先获取验证码', 'username': request.POST['用户名']})
            captcha_time = captcha.objects.filter(username_id=user.id)[0].captcha_time
            if request.POST['验证码'] != 验证码:
                return render(request, 'myauth/login.html', {'错误': '验证码错误', 'username': request.POST['用户名']})
            if (datetime.now() - captcha_time).total_seconds() >= 60:
                return render(request, 'myauth/login.html', {'错误': '验证码超时', 'username': request.POST['用户名']})
            login(request, user)
            captcha.objects.filter(username_id=user.id).update(captcha=None)
            return redirect('myauth:主页')
    else:
        return render(request, 'myauth/login.html', {'错误': 'get请求'})

def 主页(request):
    return render(request, 'myauth/index.html')

def 退出(request):
    logout(request)
    return redirect('myauth:登录页')
