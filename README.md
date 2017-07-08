# 基于Django、Amaze UI的CMS系统

### UI部分

    首先得感谢妹子UI官方网站提供的模板 [链接](http://tpl.amazeui.org/content.html?21)
    其实用妹子UI也是一个巧合，因为自己用的一直bootstrap，那天忽然在网页看到妹子UI的介绍，于是就点进去一看。
    现在国产框架已经相当成熟了，echart也是我一直在用的，所以就打算用妹子UI来写写。

### Django

#### 开发过程中的注意的一些点

    对于刚刚入门的使用，大牛请绕过。[链接](http://www.tuox.vip/2017/07/03/django/)

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

#### 体验地址

    cms.tuox.vip
    账号：test 密码 test123456
    
#### 预览

    ![电脑1](/docs/img/1.png)
    ![电脑2](/docs/img/2.png)
    ![手机端1](/docs/img/3.jpg)
    ![手机端2](/docs/img/4.jpg)



