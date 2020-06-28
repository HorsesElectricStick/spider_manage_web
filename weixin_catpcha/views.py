from django.shortcuts import render, HttpResponse
from datetime import datetime
import requests
import random
from django.contrib.auth.models import User
from weixin_catpcha.models import *

# Create your views here.

def 获取验证码(request):
    if request.method == 'POST':
        username = request.POST['用户名']
        user = User.objects.filter(username=username)
        if len(user):
            user_id = user[0].id
            token_data = captcha_API.objects.all()
            if len(token_data) < 1:
                token = 刷新token(nodata=True)
            else:
                token_time = token_data[0].token_time
                if (datetime.now() - token_time).total_seconds() >= 7200:
                    token = 刷新token()
                else:
                    token = token_data[0].token
            captcha_number = ''.join([str(random.randint(0, 9)) for i in range(6)])
            data = {
                'touser': captcha.objects.filter(username_id=user_id)[0].weixin_id,
                'template_id': 'jJb7wK-6r8g0PKyFgy2VILeD3Hdr8mS1R6bF48odzDU',
                'data': {'code': {'value': captcha_number, 'color': '#173177'}}
            }
            requests.post("https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(token),json=data)
            captcha.objects.filter(username_id=user_id).update(captcha=captcha_number, captcha_time=datetime.now())
            return HttpResponse('验证码发送成功')
    return HttpResponse('验证码发送失败')

def 刷新token(nodata=None):
    params = API_params.objects.all()[0]
    token_res = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='
                             '{}&secret={}'.format(params.app_id, params.secret))
    token = token_res.json()['access_token']
    if nodata:
        captcha_API.objects.create(token=token, token_time=datetime.now())
    else:
        captcha_API.objects.update(token=token, token_time=datetime.now())
    return token