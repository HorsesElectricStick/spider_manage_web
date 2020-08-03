from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class captcha_API(models.Model):
    token = models.CharField(max_length=300)
    token_time = models.DateTimeField()

    def __str__(self):
        return self.token_time.__str__()


class captcha(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    captcha = models.CharField(max_length=10, null=True)
    weixin_id = models.CharField(max_length=100, null=True)
    captcha_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.username.__str__()


class API_params(models.Model):
    app_id = models.CharField(max_length=50)
    secret = models.CharField(max_length=50)
