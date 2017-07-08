# 基于Django、Amaze UI的CMS系统

### UI部分

首先得感谢妹子UI官方网站提供的模板 [链接](http://tpl.amazeui.org/content.html?21)

其实用妹子UI也是一个巧合，因为自己用的一直是bootstrap，那天忽然在网页看到妹子UI的介绍，于是就点进去看一看。

现在国产框架已经相当成熟了，echart也是我一直在用的，所以就打算用妹子UI来写写。

### Django

#### 开发过程中的注意的一些点

对于刚刚入门的小伙伴使用，大牛请绕过。[链接](http://www.tuox.vip/2017/07/03/django/)

#### 使用帮助

    1.运行该环境需要的包
        pip install -r requirements.txt
    2.修改cms/cms/settings中的DATABASES节点配置，我这里使用的是MySQL，大家也可以使用SQLlite等。
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
                'NAME': '',  # 数据库名称
                'USER': '',  # 账号
                'PASSWORD': '',  # 密码
                'HOST': '',  # ip地址
                'PORT': '',  # 端口
            }
        }
    3.初始化下数据库配置 
        python manage.py makemigrations
        python manage.py migrate
    4.输入命令启动
        python manage.py runserver 0.0.0.0:5000
        默认是8000，因为我开着酷狗音乐，所以无法在本地开启，所以就占用5000吧，隔壁的flask会不会打死我。
    5.创建管理员账户
        python manage.py createsuperuser
        输入用户名、密码。
    6.进入管理员后台
        浏览器输入127.0.0.1:5000/admin
        进行菜单、用户、权限的添加、修改、删除等操作。

#### 权限说明

    1.权限配置在app为menu的config.py下
    
    设计之初为四个权限：分别为view、add、edit、delete，可以随意配置

    ("index_view", u"首页-浏览权限(index_view)")

    第一个参数是权限标识，第二个参数是权限说明

    2.使用的方法是在view前面加上一个修饰器

    @permission_required('menu.index_view', raise_exception=True)

    指定权限标识，允许抛出异常，当然这个函数也可以重定向，可以选择到自己编写的403界面或者更加友好提示的界面。

#### 一些想法

    最早打算使用iframe来做页面的跳转，后面发现体验非常不好，
    而且主题的切换也变成一个问题，无法容忍界面的不协调带来的体验，
    于是取消用iframe来做页面多开的想法。
    不然把cms后台做成一个类似于浏览器的多窗口打开，也是一个很好的体验，这个有待研究加强。

#### 更多
    
    其实还有一些贴心的小功能，比如新增了一个中间件。
    如果出错时，只有管理员才可以看到错误的页面，其余用户看到的是自定义的404或者500的页面，
    加强了用户的体验。当然你可以可以扩展下，让它变成取白名单里面的用户。
    其他更多的功能看源码咯，这里就不一一说明了。

#### 体验地址

    cms.tuox.vip
    账号：test 密码 test123456
    
#### 预览

![电脑1](/docs/img/1.png)
    
![电脑2](/docs/img/2.png)
    
![手机端1](/docs/img/3.jpg)
    
![手机端2](/docs/img/4.jpg)



