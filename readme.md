# 基于Django的爬虫管理和数据浏览平台

### 目录

+ <a style="text-decoration:none;" href="#登录系统">登录系统</a>
  + 1.1 <a style="text-decoration:none;" href="#1.1 微信验证码">微信验证码</a>







### 登录系统
----

#### 1.1 微信验证码

​		对Django的User模型进行拓展，增加微信ID字段。

​		创建了微信验证码的APP，用于对API接口的token进行定时刷新，调用微信公众号的API对指定用户的微信发送验证码。验证码默认有效期1分钟，使用过后失效。

​		微信公众号API详见：[微信公众平台](https://mp.weixin.qq.com/)

​		**\*** *token仅在调用API且token超出有效期时刷新*。

​		**\*** *本DEMO没有将消息模板写入models，如需发送其他消息模板，请在models中自行拓展*。













































<span id="112233">此处是锚点：标题一</span>