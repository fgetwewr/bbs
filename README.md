# bbs
1. ⽹站基础功能
    创建帖⼦
    修改帖⼦
    阅读帖⼦
    删除帖⼦
    查看帖⼦列表
    帖⼦列表分⻚功能 (⾃⾏实现)
    根据正⽂搜索帖⼦ Post.objects.filter(...)

2. 注册功能
  ModelForm
3. 登录功能
  密码编码处理: make_password, check_password
  from django.contrib.auth.hashers import make_password, check_password
4. 个⼈信息⻚
  昵称
  头像
  年龄
  性别
5. 头像上传功能
  模版的 form 标签添加属性: enctype=multipart/form-data
  settings 添加配置: MEDIA_ROOT, MEDIA_URL
  urls 添加处理: urlpatterns += static(settings.MEDIA_URL,
  document_root=settings.MEDIA_ROOT)
6. 退出功能
7. 以微博为例的第三⽅登录
    微博接口
    1. OAuth2.0
    1. 引导⽤户⾄授权⻚⾯
    2. ⽤户点击授权
    3. 服务器向第三⽅平台申请 Access Token
    4. 第三⽅平台回调服务器接⼝
    5. 服务器保存 Access Token
    6. 使⽤ Access Token 访问第三⽅资源
    
